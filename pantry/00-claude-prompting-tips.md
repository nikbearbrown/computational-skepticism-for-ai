# Chapter 0 — Claude Prompting Tips

## Three suggested titles

- Claude Prompting Tips: The Skill That Makes Everything Else Work
- How to Ask an AI Assistant for What You Actually Want
- Prompt Specificity: Why "Fix This" Fails and "Rewrite This for a Customer Refund" Works

---

## TL;DR

Claude (and other LLMs) respond to specificity — concrete details, constraints, and audience matter far more than politeness or length. This chapter teaches the four-move prompt structure (show what you have, say what you want, constrain it, ask for verification) that turns a vague request into useful work. The verification habit follows immediately: Claude makes plausible-sounding mistakes that cost workplaces real money, and checking the output is the professional skill that matters.

---

## Cold open

It is 4:47 PM on a Thursday. You are sitting at a desk in a regional accounting office staring at a spreadsheet you inherited from a colleague who left last week. The spreadsheet is a historical record of company expenses for the past three years — fifty rows, six columns (date, department, category, amount, approval status, notes). You have seventeen minutes before an analyst meeting, and your manager asked you in the hallway to "bring the summary of Q4 spending by department."

You have no idea what the approval status column actually means. You have no idea whether to include pending approvals. You have no idea if there's a typo in the department names (you see "Sales" and "SALES" and "sales-team"). You are staring at a problem that would take forty-five minutes to think through.

You paste the spreadsheet into Claude. You type: "Analyze this for me."

Claude returns a summary: four departments, total spend of $486,000, breakdown by category. The breakdown looks plausible. You read it. You notice it says sales spend is $180,000. You glance at the raw data. You see rows marked "Sales," "SALES," and "sales-team" — maybe 15 rows total. You do quick mental math. Fifteen rows of $10,000–$15,000 each would be $150,000–$225,000. Claude's $180,000 sits in that range, but you have no idea if it's right, and if it's wrong, your manager will look foolish in front of the analyst team.

You go back to Claude. You ask a better question: "I'm summarizing Q4 expenses by department for an internal meeting. The spreadsheet has three years of data and expense types (Travel, Equipment, Consulting, etc.). I need one number per department — total Q4 spend only. Department names seem to have formatting differences (Sales, SALES, sales-team). Should I standardize these first, or can you handle the matching? And how should I verify your groupings are right?"

Claude walks you through it. It shows you which rows it grouped into "Sales" and asks you to confirm the matching before you use the summary. It explains its reasoning. It flags that you have five rows marked "Pending" in the approval column and asks whether Q4 includes pending spend or just approved spend. You answer: approved only. Claude runs the analysis again. This time you know what went in and what comes out. You spot-check three rows in the Sales department, find they match, and use the summary.

You walk into the meeting at 5:02 with a number you trust.

The difference between the two interactions is not politeness. It is not length. It is specificity. The first prompt was vague: "Analyze this." The second prompt was specific: the audience (internal meeting), the constraint (Q4 only), the problem (name formatting), and the verification step (ask for reasoning).

Claude is a tool for thinking through a problem, not an oracle that hands you answers. The professional skill is asking the question in a way that produces thinking.

### Learning objectives

By the end of this chapter you will be able to:

- **Identify** the right Claude product (web chat, mobile app, desktop app, integrations in Word/Excel/PowerPoint/Chrome) for the task at hand.
- **Write** a specific prompt using the four-move structure (show what you have, say what you want, constrain it, ask for verification).
- **Iterate** through Claude's responses instead of starting over when the first answer misses the mark.
- **Verify** Claude's output for plausible errors before you use it in a workplace context.
- **Recognize** when you need a different approach entirely — Claude is powerful, but not everything is a Claude task.

### Prerequisites

- A Claude account (free or paid, at claude.ai or via a mobile/desktop app).
- Basic literacy with copying and pasting text.
- One workplace task you'd like Claude to help with: a memo you need to draft, data you need to analyze, a slide outline you need to structure, a formula you need to build. Bring that with you through this chapter.

### Why this chapter matters

Every chapter that follows is built on this one. When you read Chapter 3 (Word), Chapter 9 (Excel), Chapter 6 (PowerPoint), Chapter 13 (Databases), you will see Claude prompts paired with every substantive example. You will learn to write a memo, build a VLOOKUP, design a slide deck, and write a SQL query — and for each, you will see a copy-pasteable Claude prompt that does the thinking out loud and lets you verify before you commit.

This chapter teaches the prompting skill itself. By the time you finish, you will have read and understood the pattern. Every later chapter will reinforce it. By the end of the book, you will have internalized it completely.

---

## Concept 1 — Where Claude lives, and why it matters

You have an email you need to rewrite. You are sitting at your desk. You have three ways to get Claude to help:

1. Open your browser, go to claude.ai, paste the email, and type your prompt in the chat window.
2. Open your email in Outlook or Gmail, and use the Claude integration that sits right inside your email app.
3. Open your phone and use the Claude mobile app.

They all give you the same Claude — the same model, the same capabilities, the same reasoning. But they are not interchangeable in a workplace context.

### What Claude is, and how it sees the world

Claude is an LLM — a large language model, software trained on text to predict the next word in a sequence. It sounds mechanical, and it is, but the mechanics produce something that understands English well enough to write, summarize, analyze, translate, and reason through problems. Claude is one such system, made by Anthropic, a company that focuses on safety and honesty in AI.

When you send Claude a prompt (the input that elicits a response), Claude reads every word. But it does not read your files. It does not see your email inbox. It does not see your Excel spreadsheet sitting open on your screen. Claude sees only the text you give it. If the text is not there, Claude cannot see it.

This is the first principle that decides which Claude product to use.

### Claude chat (web, mobile, desktop)

Claude chat is universal. You can access it at claude.ai in any browser, on any device. You can also download a desktop app (Windows, Mac) or mobile app (iOS, Android). All three are the same interface: a text box where you type your prompt, Claude writes back, you write again, Claude responds. A conversation.

The strength of chat is portability and universality. You can use it anywhere. The weakness is data: you have to paste everything Claude needs to see. If you want Claude to help you rewrite an email, you paste the email into the chat. If you want Claude to help you analyze a spreadsheet, you paste the rows into the chat. Pasting is explicit — Claude sees exactly what you give it, nothing more. This is also why it is safe in a workplace context: you never accidentally expose files Claude should not see.

### Claude integrations (Word, Excel, PowerPoint, Chrome)

Anthropic has built Claude directly into three Microsoft Office applications (Word, Excel, PowerPoint) and into Chrome. When you use Claude within these integrations, Claude can see and edit the file you are working on. 

In Word, you open the document and click the Claude button. Claude reads the document. You type a prompt ("Summarize this in 150 words for an executive who has 10 minutes") and Claude summarizes the open document in place. No pasting required.

In Excel, you open the spreadsheet and access Claude from the ribbon. Claude sees the data in your sheet. You type a prompt ("Create a formula that sums Q4 revenue for the West region") and Claude returns a formula you can drop into a cell.

In PowerPoint, you access Claude from the ribbon. Claude sees your slides. You type a prompt ("Rewrite the speaker notes for slide 4 to be more conversational") and Claude rewrites the notes in place.

In Chrome, a Claude button appears in the browser. You navigate to a web page — a news article, a product page, a Wikipedia entry — and Claude reads the page. You type a prompt ("Extract the key claims about wind-farm efficiency") and Claude extracts them from the current page.

The strength of integrations is context: Claude can see your actual file, not a copy you pasted. The weakness is scope: integrations work inside those specific applications. If you need Claude for a quick question or for work in a different tool, you use chat instead.

### The trade-off

This is where judgment lives. A memo you are drafting in Word? Use the Claude integration in Word. Claude reads your draft, you ask it to strengthen the argument or tighten the language, and it rewrites in place. A spreadsheet analysis you are building in Excel? Use the Claude integration in Excel. Claude sees your columns, your data, your formulas, and can build or fix formulas in context.

A quick question while you are away from your desk? Use chat on your phone. A task that spans multiple files or tools? Chat might be faster — paste the pieces you need Claude to see, work through the problem, then move the pieces back where they belong. A task that spans a web page and your thinking? Use the Chrome integration to have Claude read the page, then chat to analyze it.

The trade-off is convenience (pasting takes time) versus safety (pasting makes explicit what Claude sees). In a workplace context, explicit is usually better. You know what data Claude has seen. You know what it could see. You can be confident it did not accidentally read something it should not have.

### Worked example — two ways to ask the same question

Your colleague sends you a customer email complaining about a refund delay. You need to draft a response. You have two options:

**Option 1: Web chat.**
You open claude.ai in your browser. You copy the customer email from your email app. You paste it into the chat. You type:

> **Claude prompt.** "I received this customer complaint about a refund delay. Draft a professional response acknowledging the delay, apologizing for the inconvenience, and proposing next steps. The response should be 3-4 sentences, formal but warm. Here's the customer email: [paste email]"

Claude returns a response. You read it. You paste it back into your email app.

**Option 2: Email integration (when available).**
You open the customer email in your email app. You click the Claude button. Claude reads the email directly. You type:

> **Claude prompt.** "Draft a professional response to this email: acknowledge the delay, apologize, and propose next steps. 3-4 sentences, formal but warm."

Claude writes the response right there in the reply box. You edit it if needed and send.

Both work. Option 2 is faster — no pasting. Option 1 is more explicit — you can see exactly what Claude is responding to in the chat history. Choose based on your workplace's tools and your comfort level.

### What to verify

When Claude sees your file directly (integrations), spot-check that Claude is reading the right section. If you ask Claude to summarize your Word document and Claude summarizes a different section, you know something went wrong. Chat has no such risk — you pasted exactly what you wanted Claude to see.

### Common misconceptions

**Claude is not Google.** If you ask Claude a factual question in chat (like "What is the current stock price of Apple?"), Claude does not browse the web by default. It returns what it was trained on. If you need current information, use the Claude in Chrome integration to have Claude read a web page, or use web chat (available in paid plans) that can search the internet.

**Integrations do not give Claude superpowers.** Claude in Excel is the same Claude as chat. It does not suddenly know your proprietary data or connect to a database. It sees only the file you have open. Everything you paste or see in the interface is everything Claude knows.

**"Use the one that's easiest" misses the trade-off.** Chat is universal and explicit. Integrations are fast and context-aware. Both are right for different tasks. Deciding which depends on what you are doing, not just how fast you want to move.

---

## Concept 2 — How to write a prompt that works

It is 3:15 PM. You have a paragraph that a customer received yesterday. The customer is frustrated. You need to rewrite the paragraph so it sounds more empathetic and urgent. You open Claude. You type:

> "Make this better. [paste paragraph]"

Claude returns something. It sounds nicer. It is also three times longer. You did not ask for longer. You do not know if your customer will read it. You go back to Claude and type:

> "Be more concise."

Claude cuts some words. It is still longer than you wanted. You try again:

> "Make it shorter. And more professional."

Three iterations. Fifteen minutes wasted. The frustration is not Claude's fault. It is your prompts. They are vague. Claude is answering the question you asked — *make this better* — but you were not specific about what *better* means.

### The four moves of a good prompt

A good prompt has four parts. They do not have to be separate paragraphs. But every good prompt hits all four.

**Move 1: Show what you have.** Paste the thing. Show the data. Describe the file. Claude needs to see the raw material. If you skip this, Claude has to guess, and guessing leads to useless answers. "I have a paragraph I need rewritten" is not showing. "Here's the paragraph: [paste]" is showing.

**Move 2: Say what you want.** Action verb. What should Claude do? Write? Summarize? Fix? Translate? Rewrite? Name the verb. Then name the format. Paragraph? List? Table? Bullet points? Then name the length or scope. 150 words? Five points? A 30-second version? Vague language ("make this better," "improve this," "enhance this") is the enemy. Specific language ("rewrite this as a 2-sentence summary," "translate this into plain English," "extract the five strongest claims") is the tool.

**Move 3: Constrain it.** Who is the audience? What tone should it have? What should it avoid? What is the context? "Formal" is vague. "Formal but warm, for a customer who is annoyed" is specific. "Summary" is vague. "Summary for a CEO who has 5 minutes and is deciding whether to invest" is specific. This is the move that reliably improves Claude's output. When you constrain, Claude constrains.

**Move 4: Ask for verification.** Request reasoning. Ask for alternatives. Ask Claude to flag uncertainty. Ask what it would do differently. Ask why it made a choice. The output that follows is more defensible because you know how Claude arrived at it.

### Worked example — vague prompt vs. specific prompt

**Vague version:**

> "Rewrite this email for a customer. Make it sound better."

Claude writes. You stare at it. It is friendly but maybe too casual for a refund situation. You do not know why Claude made the choices it made. You do not know what Claude was optimizing for.

**Specific version:**

> "I need to respond to a customer email about a delayed refund. The customer is frustrated but not angry. The response should:
> - Acknowledge the specific delay (mention the refund was due 5 business days ago)
> - Apologize and take responsibility
> - Explain the next step (I'll personally follow up with our finance team and email her an update within 24 hours)
> - Be 3-4 sentences, formal but warm, not overly apologetic
> 
> Here's the customer email: [paste]
> 
> Before you write the response, tell me: what tone would you aim for, and why? Then write the response. Then tell me: what would you change if the customer had expressed anger instead of frustration?"

Claude returns a paragraph on tone (you can agree or push back), then the response, then an alternative version. You now understand Claude's reasoning. You can edit one sentence and send it with confidence.

The difference is not length. The specific prompt is longer, but it is also clearer. The difference is specificity: you showed what you had, said what you wanted (3-4 sentences, formal but warm), named the constraints (acknowledge specific delay, explain next step), and asked for verification (what would change if tone was different).

### The language that reliably works

Use **action verbs**: write, draft, summarize, extract, analyze, translate, rewrite, organize, structure, list, compare, explain.

Use **constraints**: for [audience], in [format], [length], with [tone], avoiding [pitfall].

Use **specificity**: not "make it better" but "make it sound more urgent and empathetic." Not "summarize" but "summarize the key financial risk in one sentence." Not "write a list" but "write a bulleted list of five objections, from most to least common."

### The trade-off

Specific prompts take longer to write. Vague prompts are faster to type but cause iteration and waste time. A 30-second prompt that generates a useless answer costs five minutes of rework. A 90-second prompt that nails it the first time saves four minutes. Specificity is the investment that pays back immediately.

### Common misconceptions

**Longer is not better.** A 500-word prompt with multiple examples is not automatically better than a 100-word prompt with clear constraints. Write as much as you need to be specific, not a word more.

**Specifying the audience is the move that works.** Of the four moves, "constrain it" (move 3) is the one that most reliably improves Claude's output. Name the audience, and Claude's answers improve. Name the tone, and they improve further. This one move — one sentence naming who this is for — beats anything else you can do.

**"Be creative" usually makes output worse, not better.** In a workplace context, you want Claude to be specific, not creative. "Be creative with this slide copy" produces flowery, hard-to-read text. "Write slide copy that answers one question per slide" produces clarity. Save creativity for moments when you actually want it.

**Pasting examples is not always necessary.** If you are asking Claude to write an email following a standard business format, you do not need to paste an example email. You can just say "formal business email, 3 paragraphs." If you are asking Claude to match a specific tone or structure, paste an example. But it is not required every time.

---

## Concept 3 — Verifying what Claude produces

It is Wednesday. A colleague asks you to send invoices for the Q4 consulting work. You have a spreadsheet with client names, service descriptions, and billable hours. You do not have a column for the hourly rate — that is in a different sheet. You paste your spreadsheet into Claude. You ask:

> "Add a column with the invoice amount. The hourly rate for consulting is $250/hour."

Claude creates a formula and drops it in. You paste the formula into your spreadsheet. The formula references the hours column and multiplies by 250. You run it. Numbers appear. They look plausible — $2,000 here, $5,000 there, $8,000 for the big client. You send the invoices.

On Monday, a client calls. They were charged $500 when the invoice said $5,000. Your formula broke. You look at it. Claude wrote a formula that works in the example but does not lock the rate correctly when you copy it down. The column reference was not absolute, so when you copied the formula to the next row, it pointed to the wrong cell.

You had invoiced 200 clients. The pricing was wrong on 195 of them.

This is why verification matters. Claude is plausible. Claude sounds confident. Claude produces answers that *look* right. And Claude sometimes makes mistakes that cost workplaces real money.

### The verification stack

Verification has three layers. Do all three.

**Layer 1: Sanity-check the format.**
When Claude returns an answer, check the type. Did you ask for a formula? You got a formula. Did you ask for a summary? You got a summary, not a 2,000-word essay. Did you ask for a table? You got a table. This is the fast check. It takes 10 seconds and catches obvious mistakes.

**Layer 2: Check specific facts.**
Numbers, names, citations, claims — the things Claude could hallucinate. If Claude tells you the CEO's name, check it. If Claude extracts a statistic, verify the statistic exists. If Claude writes "The Federal Reserve raised rates in 2023," check whether that happened and when. If Claude builds a formula, check that it references the right columns.

**Layer 3: Test the work.**
Actually use the thing Claude produced. Run the formula on a row you know — does it return the right answer? Send the draft email to yourself — does it sound right? Use the summarized data for a decision — do the conclusions make sense? This is the expensive check because it takes time, but it is the check that catches Claude's confident mistakes.

For workplace tasks, do layer 1 always. Do layer 2 for anything with numbers or names. Do layer 3 for anything you are sending outside your desk or using for a decision.

### Worked example — verification catches an error

You ask Claude to write a VLOOKUP to match customer names from one sheet to another and return their account numbers.

Claude returns:
```
=VLOOKUP(A2, Sheet2!$A$1:$C$100, 3, FALSE)
```

**Layer 1 check:** You asked for a formula. Claude gave you a formula. Format is right.

**Layer 2 check:** You spot that Claude used column 3. You have three columns in Sheet2 (Name, ID, Account Number). Account Number is column 3. Correct. The range is locked ($A$1:$C$100). The lookup value is A2 (the first customer name). Correct.

**Layer 3 check:** You copy the formula into cell B2. You paste it down to row 50. You spot-check row 10 — you know that customer's name is "Acme Corp" and their account number should be "ACC-4521." The formula returns "ACC-4521." You check two more rows. Both are right. You run the full formula down. You spot-check one more row at random. It is right. You trust the formula.

You have just done what verification looks like.

### The trade-off

Verification takes time. A formula Claude produces instantly might take you five minutes to verify. A memo Claude drafts might take you 15 minutes to read and check. If you have 100 tasks, verification slows you down.

But an unverified formula that goes wrong costs you an hour to diagnose and fix and credibility to recover. An unverified memo that goes to a customer and sounds flat costs you the relationship. The trade-off is time now (5-15 minutes per task) versus trouble later (hours, money, reputation). The professional choice is time now.

### Common misconceptions

**A confident-sounding answer is not a correct answer.** Claude can tell you with perfect confidence that a formula works when it does not. Confidence is not evidence. Test it.

**A working example is not a working solution.** Claude might produce a formula that works on the sample data you pasted but fails on your full dataset due to edge cases (blank rows, unexpected formats, different data types). Layer 3 verification catches these.

**You cannot verify what you do not understand.** If Claude produces a complex formula or a specialized analysis and you do not understand the reasoning, ask Claude to explain it step by step before you use it. "Why did you use SUMIF instead of SUM here?" Claude can explain. If the explanation does not make sense, do not use it.

---

## Integration — three tasks, one pattern

It is 10:47 AM. You have three unrelated work tasks piling up.

**Task 1: Memo.** Your manager asked you to draft a memo to the team about updated expense policies. You have the policy document. You need a memo that summarizes the key changes in plain language.

**Task 2: Spreadsheet.** You have a Q3 sales spreadsheet with 200 rows. You need to create a formula that finds the second-highest deal size in each region.

**Task 3: Slide.** You have a presentation on product roadmap. The executive sponsor just added a new priority. You need to rewrite the "What's Next" slide to include it, keeping the same visual style.

Three tasks. Three different tools (Word, Excel, PowerPoint). Three different kinds of work (writing, formulas, design). One pattern.

### Task 1 — The memo

You open the policy document. You open a new Word doc. You paste the policy into Claude (or use the Claude integration in Word if available). You type:

> **Claude prompt.** "Summarize the key changes in this policy document in a memo format for the team. The memo should:
> - Lead with the most consequential change (probably the limit on travel approval)
> - Highlight three key differences from the old policy
> - End with 'questions? reach out to finance'
> - Be 200-250 words, plain language, friendly but professional tone
> 
> The audience is the sales team, most of whom have not read the full policy. After you write the memo, tell me: which change do you think will affect the team most, and why?"

Claude returns the memo and reasoning. You read the memo. You check the three key changes against the source document — all correct. The tone is right. You paste it into Word. You edit one sentence. You are done in 15 minutes.

**What to verify:**
- The three key changes are actually in the source document.
- The tone matches what your team expects.
- There are no glaring errors (typos, bad grammar).

### Task 2 — The spreadsheet formula

You open your sales spreadsheet. You select a cell in a new column. You use the Claude integration in Excel (or paste your data into chat Claude). You type:

> **Claude prompt.** "I need a formula to find the second-highest deal size by region. My spreadsheet has columns: Region (A), Deal_Size (B). I want the result in a new column called Second_Highest_by_Region (C). Regions repeat (multiple deals per region). The formula should return the second-largest deal size for that row's region.
> 
> Before you give me the formula, explain which function(s) you would use and why. Then write the formula. Then tell me: what edge case should I test for?"

Claude returns the explanation (you can follow the logic), the formula (something like LARGE or AGGREGATE), and the edge case (what if a region has only one deal?). You copy the formula into cell C2. You test it on a few rows. You spot-check one region you know well — the second-highest deal is right. You copy the formula down.

**What to verify:**
- The formula references the right columns.
- The formula returns a number (not an error or text).
- You test it on at least one row where you know the answer.
- You check for edge cases (what if there's a blank, what if a region has one deal).

### Task 3 — The slide rewrite

You open your PowerPoint presentation. You go to the "What's Next" slide. You see the current text ("Complete mobile app, launch API, expand to Asia"). You use the Claude integration in PowerPoint (or paste the slide content into chat Claude). You type:

> **Claude prompt.** "Rewrite this slide to include the new priority: 'Build out the enterprise security features.' Keep the same format (three bullet points, 5-7 words each). The visual already has room for four items, so add this as the fourth one and re-order by strategic importance (security first, then mobile, API, Asia). Keep the language parallel and energetic.
> 
> Tell me: what's the strategic reasoning for putting security first? Then show me the reordered list."

Claude returns the reasoning (security builds trust with enterprise clients) and the reordered list. You paste it into the slide. You read it aloud — it flows. You check that each bullet is 5-7 words. The new ordering makes sense given the company's focus on enterprise clients. You are done.

**What to verify:**
- The four items fit the visual layout.
- The language is parallel (all bullets start with verb, or all start with noun).
- The order makes strategic sense.
- The tone matches the rest of the deck.

### The pattern across all three

Each task followed the same arc:

1. **Show what you have.** Paste the policy, the spreadsheet, the slide.
2. **Say what you want.** Summarize, create a formula, rewrite.
3. **Constrain it.** Memo for the sales team, formula for each region, four bullets by strategic importance.
4. **Verify.** Check facts, test the formula, read it aloud.

By the end of this chapter, you will do this automatically. By the end of the book, you will have done it 100 times.

---

## Exercises

### Warm-up

**Exercise 0.1** — *Writing a specific prompt.* You have a paragraph that a vendor sent you describing their software's features. You need to translate it into plain language for your team. Write a prompt (don't actually run it) that asks Claude to rewrite the paragraph. Your prompt should: show what you have (paste the paragraph), say what you want (rewrite), constrain it (for your team, plain English, 3-4 sentences), and ask for verification (one question about how Claude approached it). Aim for 150-200 words.

**Exercise 0.2** — *Identifying what to verify.* Claude produces this formula:
```
=IF(A2>1000, B2*0.1, B2*0.05)
```
You asked Claude to "calculate a 10% bonus if the deal size is over $1,000, otherwise 5%." What three things would you check before using this formula in your spreadsheet?

**Exercise 0.3** — *Choosing the right Claude product.* For each task below, decide whether to use (a) chat, (b) Claude integration in Word, (c) Claude integration in Excel, (d) Claude integration in PowerPoint, or (e) Claude in Chrome. Explain your choice in one sentence.
- Analyzing a web article about AI and extracting the main claims.
- Drafting an email response to a customer complaint.
- Writing a summary of a Word document you are currently editing.
- Building a formula to match customer names to account IDs.

### Application

**Exercise 0.4** — *Spotting a vague prompt and rewriting it.* You ask Claude: "Make this clearer." Your colleague asks: "What is 'this'? Clearer for whom? What format do you want?" Rewrite your prompt to be specific. Use the four-move structure: show, say, constrain, verify.

**Exercise 0.5** — *Testing a Claude-produced summary.* Claude summarizes a 5-page policy document in 200 words. Your manager will use this summary to brief the team. Describe the three-layer verification you would do before your manager uses it. (Layer 1: sanity-check the format. Layer 2: check specific facts. Layer 3: test the work.)

**Exercise 0.6** — *Writing a prompt with constraints.* You want Claude to help you draft an apology email to a client whose project is delayed. Write a prompt that includes: what you have (the original project timeline and a note on why it's late), what you want (a draft email), and three constraints that would improve Claude's output. Aim for 100-150 words.

### Synthesis

**Exercise 0.7** — *The full four-move pattern.* You have a spreadsheet of monthly expenses. You need Claude to help you identify unusual spikes (months with 20%+ higher spending than the average). Write a complete prompt following the four-move structure: (1) show what you have, (2) say what you want, (3) constrain it, (4) ask for verification. Assume you will either paste the data into chat or use the Excel integration.

**Exercise 0.8** — *Verification design.* Imagine Claude produces an answer to this request: "Recommend five tools our team could use to manage projects." You will share these recommendations with your manager. Design a three-layer verification approach: what would you check in Layer 1 (sanity check), Layer 2 (specific facts), and Layer 3 (test the work)? For each layer, write one specific check you would perform.

### Challenge

**Exercise 0.9** — *Iterating toward the right answer.* Claude returns a memo you asked for, but it's too formal and too long. Write out: (a) a bad follow-up prompt ("Improve this"), (b) a better follow-up prompt that would move you toward what you actually want, and (c) the constraints you should have included in the first prompt to avoid the iteration. Assume the memo is for a team email, not a board meeting.

**Exercise 0.10** — *Designing a prompt for a complex task.* You need to build a quarterly revenue report. The data lives in three spreadsheets (Sales, Returns, Adjustments). You need Claude to help you decide whether to use Excel formulas or paste the data into chat for analysis. Write a prompt you would send to Claude asking for advice, then write the follow-up prompt assuming Claude recommends Excel formulas.

---

## Chapter summary

You can now do five things you could not do before you read this chapter.

You can identify which Claude product to use for a task — chat for portability and explicit control, integrations for speed and context awareness within a tool. You understand the trade-off: convenience versus visibility.

You can write a specific prompt using the four-move structure: show what you have, say what you want, constrain it, ask for verification. You know that specificity is an investment that pays back in fewer iterations and better output.

You can iterate with Claude instead of starting over. When the first answer misses the mark, you can refine the prompt rather than rage-quit and do the work manually.

You can verify what Claude produces — sanity-checking the format, checking specific facts, and testing the actual work — before you use it in a workplace context. You know that plausible-sounding answers are not the same as correct answers.

And you understand what Claude is: a tool for thinking through problems, not an oracle. The professional skill is asking the right question and verifying the answer. The AI part is the assistant. You are the thinking.

The thing to watch for, going forward, is false confidence. Claude sounds authoritative even when it is guessing. Your job is to stay skeptical, ask the question precisely, and check the work. Every later chapter in this book pairs a task with a Claude prompt. Use the four-move structure. Verify. Trust yourself to judge whether the output is right.

### What would change my mind

If Claude's capabilities shift (for example, if Claude could browse the web by default in chat, or if integrations could access multiple files at once), the specific products I recommend might change. But the core pattern — show, say, constrain, verify — would remain.

### Still puzzling

I do not yet fully understand why specificity works the way it does. Intuitively, you would think a longer, more elaborate prompt would produce better output. Instead, the wins often come from a single added constraint: naming the audience, specifying the length, or asking Claude to explain its reasoning. Why this one move — more than others — reliably improves output remains something I am still thinking through.

---

## Connections forward

Chapter 1 introduces the workplace software stack: what files are, how formats work, how applications speak to each other, and why it matters. Chapter 1 teaches the foundations of software literacy.

Chapter 3 (Creating and working in documents) is where the Claude-prompt pattern becomes routine. You will write memos, rewrite customer emails, draft formal letters — and for each, you will see a complete prompt following the four-move structure. By the end of that chapter, you will have internalized the pattern completely.

Every chapter after that reinforces it. Excel, PowerPoint, SQL, databases — each shows Claude prompts paired with real tasks. By the end of the book, you will have read and written 100+ prompts in workplace contexts. The pattern will be automatic.

The prompt is not the point. The thinking is. Claude is the tool. You are the one deciding whether the output is right.

---

## Tags

workplace-AI, prompting, claude, specification-over-length, verification, four-move-structure, workplace-software, LLM-literacy, iteration, professional-skill

