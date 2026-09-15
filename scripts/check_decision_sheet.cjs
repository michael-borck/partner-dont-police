// Offline logic test with a minimal DOM: not a browser/accessibility proof.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const html = fs.readFileSync(path.join(__dirname, "../tools/decision-sheet.html"), "utf8");
const events = {}, elements = {}, paragraphs = [], downloads = [], blobs = [];
for (const id of ["claim", "check", "decision", "export", "print", "status"]) {
  elements[id] = {
    value: "", hidden: false, textContent: "",
    addEventListener(event, callback) { events[id + ":" + event] = callback; },
    after(element) { paragraphs.push(element); }
  };
}
let printCalls = 0;
const context = vm.createContext({
  document: {
    getElementById: id => elements[id],
    querySelector: selector => ({textContent: selector}),
    createElement: tag => ({
      tag, remove() { this.removed = true; },
      click() { downloads.push(this.download); }
    }),
    body: {appendChild() {}}
  },
  Blob,
  URL: {createObjectURL(blob) {blobs.push(blob); return "blob:test";}, revokeObjectURL() {}},
  setTimeout(callback) { callback(); },
  window: {print() {
    printCalls++;
    assert.equal(paragraphs.length, 3);
    assert.equal(paragraphs[0].textContent, "4% and 5%\n<not markup>");
    assert.equal(elements.claim.hidden, true);
  }}
});
vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], context);
elements.claim.value = "4% and 5%\n<not markup>";
elements.check.value = "No profit or causal evidence.";
elements.decision.value = "Request costs and comparison design.";
events["export:click"]();
assert.deepEqual(downloads, ["pdp-m1-response.txt"]);
assert.equal(blobs[0].type, "text/plain;charset=utf-8");
(async () => {
  const exported = await blobs[0].text();
  for (const id of ["claim", "check", "decision"]) assert.ok(exported.includes(elements[id].value));
  events["print:click"]();
  assert.equal(printCalls, 1);
  assert.equal(elements.claim.hidden, false);
  assert.ok(paragraphs.every(p => p.removed));
  console.log("PASS: export payload, filename, multiline text, print content and restoration");
  console.log("Browser download, print dialog, reload and assistive-technology proof remain manual.");
})().catch(error => {console.error(error); process.exitCode = 1;});
