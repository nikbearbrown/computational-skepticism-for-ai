# Chapter 0 — Claude Code Basics

## Three possible titles

- **Your first collaborator: how to use Claude Code to write and test Python**
- **The terminal, the tool, and the loop: installing and running Claude Code**
- **Before you write a single line: Claude Code as your pair programmer**

## TL;DR

Claude Code is a command-line tool that lets you ask for code in English and watch it appear on your screen. It can write files, run them, fix them, and show you the output. This chapter teaches you to install it, ask it precisely, and verify what it produces — three skills you will use in every chapter that follows.

---

## Cold open

You open a terminal on your computer. The directory is empty except for a folder called `python-work`. You navigate into it. You type:

```
claude
```

The cursor blinks for a moment, then a prompt appears:

```
> 
```

The Claude Code agent is waiting for an instruction in English. You type:

```
create a Python script that prints "Hello from Claude Code!" and then run it to show me the output
```

You press Enter. The text appears on the screen as if someone is typing it live:

```
I'll create a Python script for you that prints the message and then run it to show the output.
```

Then a code block appears:

```python
print("Hello from Claude Code!")
```

The agent creates a file called `script.py` in your directory. You see:

```
Created file: script.py
```

Then it runs the script:

```
Running script.py...
Hello from Claude Code!
```

The output is there. The file exists. You can open it in your text editor and read it. You asked for something in English. The computer understood, acted, showed you the result, and left the code on your machine. That moment — where the request, the action, and the verification all happen in one tight loop — is what this chapter is about.

### Learning objectives

By the end of this chapter you will be able to:

- **Install** Claude Code using npm and verify the installation by running `claude`.
- **Invoke** Claude Code in a directory and write instructions that produce runnable code.
- **Request** verification by asking Claude Code to run the code and show you the output.
- **Read** and understand what Claude Code produced, and ask it to fix things that don't work.
- **Distinguish** between what an LLM says will happen and what actually happens when code runs.

### Prerequisites

- A terminal application (Terminal on macOS, Command Prompt or PowerShell on Windows, bash on Linux).
- A text editor of your choice (VS Code, Sublime Text, Notepad++, vim, or even the default editor on your system).
- Node Package Manager (`npm`) or Homebrew installed on your computer. (Instructions for installing both are in Concept 1.)
- Basic comfort with navigating a directory and running a command without a graphical interface.

### Why this chapter matters

Every chapter from Chapter 1 onward has a section called "Claude Code" where you'll ask Claude Code for Python code, verify it works, and learn from what comes back. This chapter is the prerequisite. You'll learn to install the tool once, invoke it reliably, and understand the three-part loop: specify what you want, watch it run, check if it's right. Chapters 1–15 build on this foundation.

---

## Concept 1 — Installing and invoking Claude Code

Claude Code is a command-line tool published by Anthropic. It lives in the npm package registry — the same registry where thousands of other JavaScript and Node.js tools are stored. To use it, you install it once, then run it from any directory on your computer.

### What npm is, and why we use it

npm — the Node Package Manager — is a system for sharing and installing software packages. When you install Claude Code with npm, you're downloading it to your machine and making it globally available. Think of npm like a package delivery service: you tell npm "I want Claude Code," npm fetches it from the registry, installs it where it belongs, and puts a shortcut on your PATH so you can run it from anywhere.

The PATH (a technical term borrowed from Unix) is a list of directories your terminal searches when you type a command. When you install Claude Code globally with npm, it adds a file to one of those directories. Now when you type `claude` in any terminal, your shell knows where to find it.

### Installation via npm

Here's the installation process:

**Step 1: Open a terminal.**

On macOS, open Applications → Utilities → Terminal. On Windows, press Windows key + R, type `cmd` or `powershell`, and press Enter. On Linux, open your terminal application (often accessible by pressing Ctrl+Alt+T or from your application menu).

**Step 2: Check if npm is installed.**

Type:

```bash
npm --version
```

If you see a version number (like `v20.11.0`), npm is installed. Skip to Step 4.

If you see `command not found` or a similar error, npm is not installed. Go to Step 3.

**Step 3: Install npm (if needed).**

npm comes bundled with Node.js. Download Node.js from [nodejs.org](https://nodejs.org). Choose the LTS (Long-Term Support) version. Follow the installer. Once installed, repeat Step 2 to verify.

Alternatively, if you have Homebrew installed (macOS or Linux), type:

```bash
brew install node
```

**Step 4: Install Claude Code globally.**

Type:

```bash
npm install -g @anthropic-ai/claude-code
```

The `-g` flag means "install globally" — available from any directory, not just the current one.

npm will download and install Claude Code. You should see output like:

```
added 145 packages in 23s
```

(The exact number varies. The point is: installation succeeded.)

**Step 5: Verify the installation.**

Type:

```bash
claude --version
```

If you see a version number, Claude Code is installed and ready.

### Your first session: the three-part pattern

Now you're ready to use Claude Code. Here's how a session works, illustrated with a concrete example.

**Step 1: Navigate to a working directory.**

Create a folder on your computer where you want to store your Python work. Open a terminal and navigate to it:

```bash
cd ~/python-work
```

(Replace `~/python-work` with the actual path to your folder. The `~` is a shortcut for your home directory.)

**Step 2: Start Claude Code.**

Type:

```bash
claude
```

You should see:

```
Claude Code is ready.
> 
```

Claude Code is now listening for instructions in your current directory.

**Step 3: Give it a clear instruction.**

The most important trade-off in working with Claude Code is **specificity versus terseness**. A vague instruction — "write a Python script" — might produce something close to what you wanted, but might miss the mark. A specific instruction takes a few more seconds to type but usually saves time in the long run because Claude Code gets it right the first time.

Here's a good instruction:

```
create a file called hello.py that contains one line: print("hello, world!") 
then run the file and show me the output
```

Claude Code will:
1. Create the file
2. Run it
3. Show you the output

You should see:

```
I'll create a file called hello.py with that print statement and then run it.

[Creates file: hello.py]

print("hello, world!")

[Running hello.py...]
hello, world!
```

The code is now in your directory. You can open `hello.py` in your text editor and read it.

### A common pitfall: the permission bump

The first time you install Claude Code, or if you're using it on a shared machine, you might encounter a permission error during installation. It looks like:

```
npm ERR! code EACCES
npm ERR! syscall access
```

This means npm doesn't have permission to write to the directory where global packages live. There are two fixes.

**Fix 1 (recommended): use a node version manager.**

A version manager like `nvm` (Node Version Manager) lets you install Node.js without needing root permissions. If you have time, this is the cleaner path. Instructions are at [github.com/nvm-sh/nvm](https://github.com/nvm-sh/nvm).

**Fix 2 (quick): change npm's default directory.**

Type:

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

Then try the install again:

```bash
npm install -g @anthropic-ai/claude-code
```

The last line adds `~/.npm-global/bin` to your PATH so npm-installed tools work. (You may need to add it to your shell's configuration file if you want it to persist across terminal sessions, but for now, this one export is enough to test.)

If both fixes feel beyond you, a fallback is to ask Claude Code for help: start with `npm install @anthropic-ai/claude-code` (without `-g`, local to your current directory), then run it as `npx claude` instead of just `claude`. It's slightly more typing per session, but it works if permission problems persist.

### Trade-offs: global install versus local

The trade-off here is **convenience versus clarity**.

A global install — `npm install -g @anthropic-ai/claude-code` — means you can type `claude` from any directory. One install, many uses. This is what we're doing in this chapter.

A local install — `npm install @anthropic-ai/claude-code` in a specific project folder — means Claude Code is available only in that folder, but you have clarity about versions: each project can use a different version if needed. For a beginner, global is simpler. As you grow, you might prefer local installs so projects don't interfere.

For this book, we're using global. Install once, then forget about the install process and focus on using the tool.

### Worked example — verify your installation with a hello-world

Here's a complete example you can type right now.

**Your instruction:**

```
create a file called verify.py. 
The file should contain exactly: print("Claude Code works!")
Run the file and show me the output.
```

**Claude Code's response (illustrative):**

```
I'll create verify.py and run it for you.

[Creates file: verify.py]

print("Claude Code works!")

[Running verify.py...]
Claude Code works!
```

**What you should see on your screen:**

A new file called `verify.py` in your directory, containing one line of code, and the output "Claude Code works!" printed below.

**How to verify it yourself:**

Open your text editor, open `verify.py`, and read the code. Or type:

```bash
cat verify.py
```

(On Windows, use `type verify.py`.)

You should see:

```
print("Claude Code works!")
```

### Common misconceptions

**Claude Code is not a code editor.** You don't write code in Claude Code the way you write in VS Code or Sublime. Claude Code is an agent — it reads your instructions, creates and modifies files, runs them, and reports results. Your text editor is for reading and manually editing files.

**Claude Code is not Python.** Claude Code is a tool that works with Python (and other languages). When Claude Code runs a Python file, it's using your system's Python interpreter. Claude Code itself is written in JavaScript and runs in Node.js.

**"Run the code" is not optional.** An LLM can *describe* what code will do without actually running it. That description is often subtly wrong. Always ask Claude Code to run the code and show you the output. The output is the truth.

**Claude Code asks for permission.** Some operations — deleting files, modifying sensitive parts of your system — require your approval. You'll see a prompt asking "Should I do this?" You choose yes or no. The human is always in the loop.

---

## Concept 2 — How to instruct Claude Code effectively

The second most important skill after installation is writing good instructions. An instruction to Claude Code should be specific enough that Claude Code has a real chance of getting it right, but concise enough that you're not writing an essay.

### The specification trade-off

Here's the core trade-off: **verbose specifications are slower to type but faster to execute; minimal specifications are quick to write but often require iteration.**

A minimal specification:

```
write a function that adds two numbers
```

This is fast to type. But "function that adds two numbers" could mean:
- A function named `add` or `sum_numbers`?
- Takes two arguments or accepts a list?
- Returns the result or prints it?
- Should it work with integers, floats, or both?

Claude Code will guess. It might get it right. It might not. Then you iterate: "No, I meant take two arguments as floats and return the result." That's a second round trip.

A specific specification:

```
create a function called add_prices that takes two arguments, price1 and price2 (both floats), 
adds them, and returns the result. 
put it in a file called math_tools.py. 
test it by calling add_prices(10.50, 20.25) and printing the result. 
run the file and show me the output.
```

This is longer to type. But Claude Code understands exactly what you want. One round trip, done.

### The anatomy of a good instruction

A good instruction has four parts:

1. **What to create or modify.** "Create a file called `greeting.py`" or "Edit the function `process_data` in `data.py`."

2. **What the code should do.** "The function should take a name as input, concatenate it with 'Hello, ', and return the result."

3. **How to test or verify.** "Call it with the input 'Alice' and print the result."

4. **What to show you.** "Run the file and show me the output."

Here's an example with all four parts:

```
create a file called fahrenheit.py
that contains a function called convert_f_to_c that takes one argument, temp_f (a float), 
and returns the Celsius equivalent using the formula (temp_f - 32) * 5/9.
test it by calling convert_f_to_c(98.6) and printing the result.
run the file and show me the output.
```

Claude Code will:
1. Create `fahrenheit.py`
2. Write the function
3. Add a test call
4. Run the file
5. Show you the output

You see everything: the code, the output, and confirmation that the code works.

### Named parameters and edge cases

When a function has parameters, name them in your instruction. Don't say "takes two numbers." Say "takes two arguments: start (an integer) and end (an integer)."

When you care about edge cases, mention them:

```
create a function called safe_divide that takes two arguments, numerator and denominator (both floats).
if denominator is 0, return 0 instead of raising an error.
otherwise, return numerator / denominator.
test it with safe_divide(10, 2), safe_divide(10, 0), and safe_divide(7, 3).
run the file and show me the output.
```

The instruction is longer, but Claude Code won't miss the edge case.

### The permission loop

Some operations require your permission. If Claude Code is about to delete a file, modify your system, or write to a sensitive directory, it will ask:

```
Should I delete the file "old_data.csv"? [yes/no]
```

You type `yes` or `no`. The human always has the final say.

This is a feature, not a bug. It prevents accidents.

### Worked example — a three-part Claude Code session

Here's a realistic example showing specification, execution, and verification.

**Your instruction (specific and clear):**

```
create a file called greet.py.
the file should ask the user for their name using input("What's your name? "),
store the result in a variable called name,
then print "Hello, " + name + "!".
test it by simulating user input of "Alex".
run the file and show me the output.
```

**Claude Code's response (illustrative):**

```
I'll create greet.py with that input and output logic.

[Creates file: greet.py]

name = input("What's your name? ")
print("Hello, " + name + "!")

[Running greet.py with input "Alex"...]
What's your name? Alex
Hello, Alex!
```

**What you verify:**

The code is correct. The output shows the prompt, then the input, then the greeting. The program works as specified.

**If something went wrong:**

Say Claude Code printed "Hello, Alex!" on the same line as the prompt. You'd ask:

```
the output should show the prompt on one line, then "Hello, Alex!" on the next line. 
can you check the code and fix it if needed?
```

Claude Code would run it again, see the issue (if there is one), and fix it.

### Common misconceptions

**"Make it work" is too vague.** Claude Code has no context about what "work" means. Does the code need to run without errors? Produce specific output? Handle edge cases? Be fast? Always specify what "work" means.

**Claude Code can read files in your directory.** If you're modifying an existing file, Claude Code can open it, see what's there, and make changes. You don't have to paste the whole file into your instruction. Just say "edit the file `process.py` to..." and Claude Code will handle it.

**You can ask Claude Code to read its own output.** If Claude Code creates a file, runs it, and sees unexpected output, you can ask it to investigate: "The output shows a bug. Can you look at the code and find the problem?" Claude Code can read files and reason about what went wrong.

---

## Concept 3 — Verifying what Claude Code produces

The third cornerstone of working with Claude Code is verification. An LLM can write code that *looks* right but has subtle bugs. Running the code is the verification. Reading the output is how you know whether to trust it.

### Why running beats describing

When Claude Code says "the code will output X," that's a prediction. Predictions from LLMs are often right, but sometimes wrong in ways that matter. When Claude Code actually runs the code and shows you the output, that's a fact.

Example: Claude Code might produce code that runs without error but produces the wrong number because of an off-by-one mistake, or because it misunderstood the logic. The only way to catch this is to run it and look.

**Always ask Claude Code to run the code and show you the output.** Don't ask "is this right?" Ask "run it and show me what happens."

### Three levels of verification

**Level 1: The code runs without error.**

The simplest check: did the code execute, or did it crash? If it crashed, you see an error message. Claude Code can read the error and fix it.

Example:

```
write a function called double that takes one argument x and returns 2 * x.
call double(5) and print the result.
run the file and show me the output.
```

Claude Code runs it. You see:

```
10
```

No error. Good.

**Level 2: The output is what you expected.**

The code ran without error, but does it produce the *right* answer?

Example:

```
write a function called sum_three that takes three arguments a, b, c and returns a + b + c.
test it: sum_three(1, 2, 3) should give 6.
sum_three(10, 20, 30) should give 60.
run the file and show me the output of both tests.
```

Claude Code runs it. You see:

```
Test 1: 6
Test 2: 60
```

Both are correct. The function works as specified.

**Level 3: The code handles edge cases.**

Beyond the happy path, does the code handle unusual inputs?

Example:

```
write a function called safe_divide that takes two numbers, numerator and denominator.
if denominator is 0, return the string "Cannot divide by zero".
otherwise, return numerator / denominator (as a float).
test it: safe_divide(10, 2) should give 5.0. safe_divide(10, 0) should give "Cannot divide by zero".
run the file and show me the output.
```

Claude Code runs it. You see:

```
Test 1: 5.0
Test 2: Cannot divide by zero
```

The function handles both the normal case and the edge case.

### Reading tracebacks

When code crashes, Python prints a traceback — a detailed report of what went wrong and where. Learning to read a traceback is a crucial skill.

Example traceback:

```
Traceback (most recent call last):
  File "script.py", line 3, in <module>
    result = 10 / denominator
ZeroDivisionError: division by zero
```

Read it bottom-up:
- **The error type:** `ZeroDivisionError` — you tried to divide by zero.
- **The line that failed:** `result = 10 / denominator` on line 3.
- **The file:** `script.py`.

Once you know what went wrong, you ask Claude Code to fix it:

```
the code failed with "ZeroDivisionError: division by zero" on the line "result = 10 / denominator".
can you fix it by checking if denominator is 0 before dividing?
```

Claude Code will update the code and run it again.

### The test-driven verification loop

Here's a pattern that works well: **write tests before asking Claude Code to implement.**

Instead of:

```
write a function that calculates the distance between two points
```

Write:

```
write a function called distance that takes four arguments: x1, y1, x2, y2 (all floats).
it should calculate the Euclidean distance using sqrt((x2-x1)^2 + (y2-y1)^2).
test cases:
  distance(0, 0, 3, 4) should give 5.0 (the 3-4-5 triangle)
  distance(0, 0, 0, 0) should give 0.0
  distance(1, 1, 4, 5) should give 5.0
run the file and show me the output of all three tests.
```

Now Claude Code knows exactly what you want, and the tests verify that it got it right.

### Worked example — catching a subtle bug through testing

**Your instruction:**

```
write a function called count_up that takes one argument, n (an integer).
the function should print the numbers from 1 to n (inclusive).
test it: count_up(3) should print:
1
2
3
call count_up(3) and run the file to show me the output.
```

**Claude Code's response (illustrative):**

```
I'll create the function and test it.

[Creates file: count_up.py]

def count_up(n):
    for i in range(n):
        print(i)

count_up(3)

[Running count_up.py...]
0
1
2
```

**What you notice:**

The output is `0, 1, 2` but you expected `1, 2, 3`. The function is off by one. `range(n)` counts from 0 to n-1, not 1 to n.

**You ask Claude Code to fix it:**

```
the function count_up(3) printed 0, 1, 2 but it should print 1, 2, 3. 
the issue is that range(n) starts at 0. 
can you fix it to use range(1, n+1) instead?
```

Claude Code updates the code:

```
def count_up(n):
    for i in range(1, n+1):
        print(i)

count_up(3)

[Running count_up.py...]
1
2
3
```

Now it's correct. You caught the bug through testing.

### Trade-off: trust speed versus verification cost

Writing tests takes time. Running the code takes time. But skipping verification causes problems later: a subtle bug makes its way into your program, and you waste hours debugging.

The trade-off:

- **Fast path:** Ask Claude Code to write and run code, glance at the output, assume it's right. Risk: subtle bugs slip through.
- **Safe path:** Write specific tests, ask Claude Code to run them, verify each one passes. Risk: you spend more time upfront.

For homework and learning, the safe path is worth it. You're building confidence in the code and in yourself. Later, when you're writing code professionally, you'll lean on automated tests (a skill this book introduces in Chapter 6).

### Common misconceptions

**A passing run is not a passing test.** Code that runs without error might still be wrong. `print(5)` runs without error, but if you wanted `print(10)`, the code is wrong.

**The LLM's word is not evidence.** If Claude Code says "this should output 42," that's not the same as running it and seeing 42 on the screen. Always ask for the actual output.

**Fixing one bug doesn't guarantee no other bugs.** When Claude Code fixes a bug you found, ask it to run all your tests again, not just the one that was broken.

---

## Integration — the three-part loop in action

Here's a complete example that exercises all three concepts: installing, specifying, and verifying.

You've installed Claude Code. You open a terminal, navigate to your `python-work` directory, and start a session:

```bash
cd ~/python-work
claude
```

You're now at the `>` prompt. You want to write a program that converts temperatures from Celsius to Fahrenheit. You give Claude Code a specific instruction:

```
create a file called temp_convert.py.
the file should contain a function called celsius_to_fahrenheit that takes one argument: celsius (a float).
the function should return fahrenheit using the formula celsius * 9/5 + 32.
test the function with these cases:
  celsius_to_fahrenheit(0) should return 32.0 (water freezes)
  celsius_to_fahrenheit(100) should return 212.0 (water boils)
  celsius_to_fahrenheit(37) should return approximately 98.6 (body temperature)
then call each test and print the results.
run the file and show me the output of all three tests.
```

Claude Code responds (illustrative):

```
I'll create the function with those specific test cases.

[Creates file: temp_convert.py]

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Test cases
print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"37°C = {celsius_to_fahrenheit(37)}°F")

[Running temp_convert.py...]
0°C = 32.0°F
100°C = 212.0°F
37°C = {98.6}°F
```

You check the output against your expectations:
- 0°C → 32°F ✓
- 100°C → 212°F ✓
- 37°C → 98.6°F ✓

All three tests pass. The code is correct. You open `temp_convert.py` in your text editor and read the function to understand how it works. You are confident in the code because you specified it precisely, Claude Code ran it, and the output matched your expectations.

Later chapters will add complexity — functions with multiple parameters, loops, data structures, tests with pytest — but the loop stays the same: specify, execute, verify.

---

## Exercises

### Warm-up: install and run

Install Claude Code (if you haven't already) and verify the installation by running:

```bash
claude --version
```

Then start a Claude Code session:

```bash
claude
```

And type:

```
create a file called test.py that prints "Claude Code is ready!".
run the file and show me the output.
```

Stop the session by typing `exit` or pressing Ctrl+D.

### Application: the welcome program

Start a Claude Code session in your `python-work` directory and ask Claude Code to:

```
create a file called welcome.py.
the file should ask the user for their name using input("Enter your name: ").
store the name in a variable.
print a welcome message like "Welcome to Python, [name]!".
test it by simulating the input "Jordan".
run the file and show me the output.
```

Verify that the output matches what you expected. Open `welcome.py` in your text editor and read the code.

### Synthesis: the calculator function

Ask Claude Code to:

```
create a file called calc.py.
write a function called add_and_multiply that takes three arguments: a, b, c (all floats or integers).
the function should return (a + b) * c.
test the function with these cases:
  add_and_multiply(2, 3, 4) should return 20 (because (2+3)*4 = 20)
  add_and_multiply(10, 5, 2) should return 30 (because (10+5)*2 = 30)
  add_and_multiply(1, 1, 1) should return 2 (because (1+1)*1 = 2)
run the file and show me the output of all three tests.
```

Verify each test. If one fails, ask Claude Code what went wrong and fix it.

### Challenge: error handling

Ask Claude Code to:

```
create a file called safe_calc.py.
write a function called safe_add that takes two arguments: a and b.
if either a or b is not a number (check with isinstance(a, (int, float))), return the string "Error: invalid input".
otherwise, return a + b.
test it with:
  safe_add(5, 3) should return 8
  safe_add(5, "hello") should return "Error: invalid input"
run the file and show me the output of both tests.
```

This exercise introduces error checking — a real skill you'll use throughout the book.

---

## Chapter summary

You have now learned three skills:

**Skill 1: Installation.** Claude Code installs via npm as a global package. One install, many uses. You can run it from any directory on your computer.

**Skill 2: Instruction.** Clear instructions to Claude Code are specific about what to create, what it should do, how to test it, and what to show you. Specificity costs a few extra seconds but saves rounds of iteration.

**Skill 3: Verification.** You always ask Claude Code to run the code and show you the output. A prediction from an LLM is not the same as actual execution. The output is the truth.

The loop you've learned — specify, execute, verify — is the same loop you'll run in every chapter that follows. Every chapter from Chapter 1 onward has a "Claude Code" section. In Chapter 1, you'll use this loop to understand statements and output. In Chapter 2, you'll use it to explore expressions. By Chapter 15, you'll have run 15+ Claude Code sessions, and the loop will be muscle memory.

The misconception to watch for: Claude Code is not a replacement for understanding what good code looks like. Claude Code is a collaborator. Your job is to specify precisely, understand what comes back, and know whether to accept it or ask for changes. That judgment — knowing good code when you see it — comes from reading code, running it, and thinking about how it works. This book teaches you to do that.

---

## Connections forward

Every chapter from here on has at least one "Claude Code" section. Here's how they work:

**Chapter 1 — Statements:** You'll ask Claude Code to write `print()` statements and `input()` functions, then run them and read the output.

**Chapter 2 — Expressions:** You'll specify arithmetic expressions, ask Claude Code to evaluate them, and verify that the precedence is what you expected.

**Chapters 3–6:** As you learn about objects, decisions, loops, and functions, Claude Code will be your pair programmer. You specify the logic, it writes the code, you verify it works.

**Chapter 6 onwards:** You'll learn to write tests with pytest, and Claude Code will run those tests for you, showing which ones pass and which ones fail.

**By Chapter 15:** You'll be so comfortable with the loop — specify, run, verify — that you'll use it to explore data science libraries like NumPy and pandas without thinking twice.

The tool is the same. The loop is the same. Only the concepts you're exploring get more advanced.

---

## What would change my mind

If Claude Code significantly changes how it works — if it stops asking for permission, or stops showing file output, or removes the ability to run code — then the instruction model in this chapter would need updating. Until then, the three-part loop (specify, execute, verify) remains the foundation.

## Still puzzling

I'm still working through the best way to explain why "verify by running" matters so much in the LLM era. The intuition is clear — running code is the ground truth — but the deeper question of how much trust to place in LLM-written code, and when to read it versus when to just run it, is something I don't fully understand yet.

---

## Tags

claude-code, tools, installation, npm, verification, LLM-collaboration, testing, command-line, first-principles, pair-programming
