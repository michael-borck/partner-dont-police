# AI as a Teaching Partner: Practical Applications for Multidisciplinary Business Education

A comprehensive guide for educators integrating AI into teaching across business disciplines including HR, marketing, accounting, management, supply chain, information systems, tourism & hospitality, and economics.

## Overview

This Quarto book provides practical, evidence-based approaches to using generative AI as a teaching partner in business education. Rather than viewing AI as a threat to academic integrity, it reframes AI as a tool for enhancing learning through:

- **Flight Simulator Learning**: Safe practice environments where students can learn from AI feedback without stakes
- **Process-Based Assessment**: Evaluating how students think, not just what they produce
- **Transparent AI Use**: Making AI use explicit and building critical engagement skills
- **Discipline-Specific Applications**: Real examples from 8+ business disciplines

## Features

### 18 Main Chapters
1. **Introduction** - The problem we're solving and core principles
2. **Getting Started** - CRAFT framework for structured prompting
3. **Discovering Your Teaching Strategy** - Using AI to discover your personal AI strategy
4. **First Steps** - Week-by-week implementation guidance
5. **Seven Essential Techniques** - Core prompt engineering techniques (including prompt chaining)
6. **Managing LLM Context** - Working smarter with AI conversations and managing long-form interactions
7. **Flight Simulator** - Creating realistic practice scenarios
8. **Critique Toolkit** - Teaching students to evaluate AI critically
9. **Ethics, Data Governance & Integrity** - Transparent approaches to AI use with data protection
10. **Process Assessment** - Assessing thinking, not just outputs
11. **Self-Assessment** - Building student metacognition with AI
12. **Virtual Company** - Sustained simulation learning
13. **Unit Design** - Integrating AI across full units
14. **Static to Interactive** - Converting existing content to AI-enhanced learning
15. **From Conversation to Document** - Creating professional deliverables (Word, PowerPoint, Excel) from AI conversations
16. **Research Assistant** - AI for postgraduate research
17. **Advanced Frontiers** - Agents, automation, RAG, emerging capabilities
18. **Conclusion** - Bringing it all together

### 4 Appendices
- **Prompt Library** - Ready-to-use prompts with cross-discipline adaptations
- **Workshop Guide** - Practical training materials for colleagues
- **Curtin Alignment** - Institutional alignment with learning outcomes
- **Advanced Prompting** - Deep dive into sophisticated prompting techniques

### Multidisciplinary Approach

All major examples appear in **8 different business disciplines**:
- Human Resources
- Business & Marketing
- Accounting & Finance
- Management & Organisational Studies
- Supply Chain & Logistics
- Information Systems
- Tourism & Hospitality
- Economics

Complex prompts and detailed examples use **Quarto's tabbed interface** so readers can see their discipline's perspective.

## Getting Started

### Prerequisites
- [Quarto](https://quarto.org) (version 1.3 or later)
- A text editor or IDE (VS Code, RStudio, etc.)
- Optional: [Pandoc](https://pandoc.org/) for PDF output

### Building the Book

```bash
# Build HTML version
quarto render

# Build specific format
quarto render --to html
quarto render --to pdf

# Preview while editing
quarto preview
```

Output will be in the `_book/` directory.

### Customizing for Your Institution

The book is designed around Curtin University but can be easily adapted:

1. **Update title and author** in `_quarto.yml`
2. **Modify examples** to reference your institution
3. **Adjust learning outcomes** in appendix C to match your program
4. **Update institutional policies** in relevant chapters
5. **Add discipline-specific content** using the existing tabbed structure

## Project Structure

```
├── README.md                    # This file
├── _quarto.yml                 # Quarto book configuration
├── index.qmd                   # Book introduction and navigation
├── introduction.qmd            # Chapter 1: Core concepts
├── getting-started.qmd         # Chapter 2: CRAFT framework
├── discovering-your-strategy.qmd # Chapter 3: Finding your AI teaching strategy
├── first-steps.qmd             # Chapter 4: Implementation timeline
├── seven-techniques.qmd        # Chapter 5: Core prompting techniques
├── managing-context.qmd        # Chapter 6: Managing LLM context
├── flight-simulator.qmd        # Chapter 7: Practice scenarios
├── critique-toolkit.qmd        # Chapter 8: Critical evaluation
├── ethics-integrity.qmd        # Chapter 9: Data governance & integrity
├── process-assessment.qmd      # Chapter 10: Assessing thinking
├── self-assessment.qmd         # Chapter 11: Student metacognition
├── virtual-company.qmd         # Chapter 12: Sustained simulation
├── unit-design.qmd             # Chapter 13: Full unit design
├── static-to-interactive.qmd   # Chapter 14: Converting static content
├── from-conversation-to-document.qmd # Chapter 15: Creating documents from AI
├── research-assistant.qmd      # Chapter 16: Research support
├── advanced-frontiers.qmd      # Chapter 17: Agents & automation
├── conclusion.qmd              # Chapter 18: Bringing it together
├── prompt-library.qmd          # Appendix A: Ready-to-use prompts
├── workshop-guide.qmd          # Appendix B: Training materials
├── curtin-alignment.qmd        # Appendix C: Institutional alignment
└── advanced-prompting.qmd           # Appendix D: Advanced techniques
```

## Key Concepts

### Flight Simulator Learning
AI conversations can function like flight simulators—allowing students to practice complex professional scenarios repeatedly with immediate, realistic feedback, without the stakes of real situations.

### Transparent AI Use
Rather than prohibiting AI, the approach makes AI use explicit:
- Students use AI openly in assignments
- They must show their thinking process
- They critique and verify AI outputs
- They're assessed on their judgment, not the AI's output

### Process-Based Assessment
Shift evaluation from "what did the AI produce?" to:
- What was the quality of the prompt?
- How did the student evaluate the response?
- What judgment did they apply?
- How did they improve the output?

### Discipline-Specific Pedagogy
Each business discipline has unique AI applications:
- **HR**: Scenario simulation, policy development, stakeholder communication
- **Marketing**: Campaign strategy, customer analysis, content optimization
- **Accounting**: Audit findings, compliance communication, financial analysis
- **Management**: Change management, organisational design, stakeholder engagement
- **Supply Chain**: Vendor negotiation, crisis response, process optimization
- **IT/IS**: Requirements gathering, system documentation, change management
- **Tourism & Hospitality**: Service recovery, guest relations, revenue optimization
- **Economics**: Data analysis, policy analysis, trend interpretation

## Using This Book

### For Individual Educators
1. Read Chapter 1 to understand the pedagogical approach
2. Choose one application from your discipline
3. Try one small experiment (Chapter 2 has easy starting points)
4. Adapt a prompt from the Prompt Library for your teaching
5. Gradually expand based on student feedback

### For Program Curriculum Teams
1. Review learning outcomes alignment (Appendix C)
2. Map AI applications across the full program
3. Develop shared prompts and scenarios
4. Create consistency in how AI is used across units
5. Establish academic integrity policies informed by Chapter 8

### For Faculty Development
Use Appendix B (Workshop Guide) for colleague training that:
- Builds understanding of the pedagogical approach
- Demonstrates practical implementations
- Addresses concerns and misconceptions
- Provides hands-on practice with prompts

### For Institutional Leaders
- Chapter 1 outlines the strategic rationale
- Appendix C shows alignment with institutional priorities
- Evidence of pedagogical effectiveness (throughout book)
- Implementation timeline and resource requirements (Chapter 3)

## Core Pedagogical Principles

1. **AI as Scaffolding** - AI supports learning through meaningful challenge, not by removing effort
2. **Transparency Over Prohibition** - Open AI use builds better practices than hidden use
3. **Process Over Output** - Assess how students think, not what AI produces
4. **Authentic Practice** - Simulations match professional reality
5. **Critical Engagement** - Students learn to evaluate and improve AI outputs
6. **Discipline-Specific Context** - Applications reflect how professionals actually work
7. **Gradual Sophistication** - Start simple, add complexity progressively

## Customization Guide

### For a Specific Discipline

1. Update `_quarto.yml` title to include your discipline
2. In each chapter, emphasize your discipline's tabs when creating examples
3. Add discipline-specific learning outcomes to Chapter 1
4. Customize Chapter 13 (Unit Design) with your program's structure
5. Update Appendix C with your institution's alignment

### For a Different Institution

1. Search for "Curtin" and replace with your institution name
2. Update Appendix C learning outcomes to match your program
3. Modify Chapter 4 (First Steps) implementation timeline if needed
4. Update any institutional policy references
5. Adjust examples to match your local context

### For Advanced Users

Appendix D (Advanced Prompting) provides techniques for:
- Creating consistent persona definitions
- Managing complex conversational contexts
- Implementing quality control mechanisms
- Building sophisticated assessment templates
- Generating discipline-specific educational materials

## Building AI Skills in Students

The book develops three levels of AI competency:

**Level 1: Basic Use**
- Chapters 2-5 teach using AI to practice and explore
- Students use simple prompts with basic feedback loops

**Level 2: Strategic Use**
- Chapters 6-9 teach prompting techniques and critical evaluation
- Students craft sophisticated prompts and evaluate outputs

**Level 3: Professional Integration**
- Chapters 10-17 show how professionals integrate AI into work
- Students apply AI responsibly in authentic scenarios

## Implementation Timeline

### Week 1: Foundation
- Read Chapter 1 (understanding)
- Review your discipline's examples throughout

### Week 2: First Application
- Choose one small experiment from Chapter 2
- Try a prompt from the Prompt Library

### Week 3-4: Expansion
- Add second application
- Gather student feedback
- Refine approach based on results

### Month 2-3: Integration
- Implement across a unit (Chapter 13)
- Develop shared resources with colleagues
- Address academic integrity questions (Chapter 9)

### Ongoing
- Scale to more units
- Measure impact on learning outcomes
- Share innovations with professional bodies

## Academic Integrity Approach

Rather than trying to detect and prevent AI use, this book teaches:

1. **Transparent Use** - Students declare AI use explicitly
2. **Critical Engagement** - Students verify and improve AI outputs
3. **Process Evidence** - Students show their thinking in transcripts/logs
4. **Professional Ethics** - Students learn how professionals use AI responsibly
5. **Institutional Alignment** - Policies support learning, not punishment

See Chapter 8 and Appendix C for full guidance.

## Prompt Library

Over 100 ready-to-use prompts organised by:
- Application type (simulation, assessment, content creation, etc.)
- Discipline (8 business fields)
- Complexity level (beginner to advanced)
- Chapter reference (where to use in curriculum)

All prompts can be adapted to your specific context—simply adjust the discipline, scenario details, or role descriptions.

## Support and Adaptation

### Common Questions Addressed

**"Will students just use the AI output without thinking?"**
→ See Chapter 10 on process-based assessment and Chapter 7 on flight simulator design

**"How do I address academic integrity concerns?"**
→ See Chapter 9 on transparent approaches and Appendix C on institutional alignment

**"How do I start small?"**
→ See Chapter 2 (Getting Started) and Chapter 4 (First Steps)

**"How is this different from just letting students use ChatGPT?"**
→ See Chapter 1 on Flight Simulator learning and Chapter 8 on critical evaluation

**"Which examples apply to my discipline?"**
→ Each section has tabbed examples for 8+ business disciplines

## Contributing to This Book

If you adapt this book for your institution or discover improvements:

1. Document what worked well
2. Note any sections that were unclear
3. Contribute discipline-specific examples
4. Share your implementation results

This living document benefits from educator feedback.

## Recommended Reading Order

### For Quick Start
1. Chapter 1 (30 min) - Understand the approach
2. Chapter 2 (45 min) - See first applications
3. Your discipline's examples throughout
4. Appendix A - Find a prompt to try

### For Comprehensive Understanding
Read in book order (each chapter builds on previous):
1. Introduction
2. Getting Started
3. Discovering Your Teaching Strategy
4. First Steps
5. Seven Techniques
6. Managing LLM Context
7-16. Each chapter as you plan implementation
17. Conclusion - synthesis and vision

### For Program Design
1. Chapter 1 - Pedagogical foundation
2. Chapter 13 - Unit design framework
3. Appendix C - Learning outcome alignment
4. Chapter 9 - Academic integrity approach
5. Appendix B - Faculty development

## Technical Requirements

- Quarto 1.3+
- Modern web browser for HTML version
- PDF reader for PDF output
- Optional: RStudio or VS Code for editing

## License and Use

This book is provided as a resource for educators. You are free to:
- Use it with your students
- Adapt it for your institution
- Share adapted versions
- Incorporate examples in your teaching

## Citation

If referencing this material in academic contexts:

```
AI as a Teaching Partner: Practical Applications for Multidisciplinary Business Education
[Institution], [Year]
```

## Acknowledgments

This resource draws on:
- Experiential learning theory (Kolb)
- Deliberate practice frameworks
- Authentic assessment principles
- Contemporary pedagogical research on AI in education

## Contact and Feedback

For questions, suggestions, or to share your implementation experience, please reach out to your institution's teaching and learning support team.

---

**Version**: 1.0 (Multidisciplinary Edition)
**Last Updated**: 2024
**Book Format**: Quarto HTML/PDF

Built with Quarto - https://quarto.org
