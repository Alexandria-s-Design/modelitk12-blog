---
layout: post
title: "The 20-Minute Challenge: Build Your First Model Right Now"
date: 2025-12-15 08:00:00 -0500
category: "Hands-On Guide"
author: "Dr. Charles & Dr. Marie Martin"
hero_image: "/assets/images/week7-hero.jpg"
excerpt: "Stop reading. Start building. This step-by-step guide walks you through creating an actual computational model in 20 minutes—with zero prior experience required."
---

## Enough Theory. Time to Build.

For six weeks, we've told you about modeling:
- Why it matters (NGSS alignment)
- What it can do (systems thinking)
- Who built it (research foundation)

**Today, you're going to build a model.**

Not read about building. Not watch someone else build.

**You're actually going to do it.**

**Time required**: 20 minutes
**Skills required**: None
**What you need**: Computer, browser, this guide

**Ready?**

## The Model You're Building: Enzyme Regulation

We're modeling a simple but powerful biological system:

**An enzyme that's controlled by feedback inhibition.**

This shows up everywhere in biology:
- Glycolysis (ATP inhibits phosphofructokinase)
- Amino acid synthesis (end product inhibits first enzyme)
- Purine synthesis (AMP/GMP inhibit PRPP amidotransferase)

**It's simple enough to build in 20 minutes. Complex enough to teach real concepts.**

**By the end, you'll have**:
- A working network model
- Simulation results showing feedback control
- Data you can use for a CER argument
- Confidence to do this with students

**Let's go.**

## Step 1: Open Cell Collective (2 minutes)

### What to do:

1. Go to **[cellcollective.org](https://cellcollective.org)**
2. Click **"Create Account"** or **"Sign In"** (if you already have one)
3. Once logged in, look for **"Create New Model"** or **"My Models"**

**Note**: You can browse models without an account, but you'll need one to create and save your own.

### What you'll see:

A dashboard with:
- Library of public models
- Your saved models (empty if you're new)
- A button to create a new model

### Click "Create New Model"

You'll be prompted for:
- **Model Name**: Call it "Enzyme Feedback Regulation"
- **Description** (optional): "Simple model showing how product inhibits enzyme activity"

Click **"Create"** (or "OK" or "Save")

**You're in.**

## Step 2: Add Your Components (5 minutes)

You're looking at a blank canvas. This is where you build your network.

### The components you need:

1. **Substrate** (input - what the enzyme acts on)
2. **Enzyme** (the catalyst)
3. **Product** (output - what the enzyme produces)
4. **Inhibitor** (we'll use Product itself as the inhibitor - that's the feedback!)

### How to add them:

**Look for a button or panel that says**:
- "Add Component" OR
- "Add Node" OR
- A "+" icon in a component panel

**For each component**:
1. Click "Add Component"
2. Type the name: "Substrate"
3. (Optional) Add a description: "Molecule that enzyme converts to product"
4. Click "Add" or "Save"

**Repeat for**:
- **Enzyme** - "Catalyzes substrate → product reaction"
- **Product** - "End result of enzyme activity"

**You now have 3 nodes on your canvas.**

### Visual tip:

Arrange them in a line (left to right) so you can see the flow:

```
Substrate → Enzyme → Product
```

Later we'll add the feedback arrow back from Product to Enzyme.

## Step 3: Connect the Components (3 minutes)

Now we define **relationships**: Who affects whom?

### The connections you need:

1. **Substrate → Enzyme** (Substrate is required for enzyme to work)
2. **Enzyme → Product** (Enzyme produces Product)
3. **Product → Enzyme** (Product inhibits Enzyme - feedback!)

### How to make connections:

**Look for a tool that says**:
- "Add Edge" OR
- "Add Relationship" OR
- "Connect" OR
- A drawing tool (arrow icon)

**Method 1**: Click and drag from one node to another
**Method 2**: Select a node, then click "Add Regulator" and choose another node

### Create these three connections:

#### Connection 1: Substrate → Enzyme (Activation)

- Click **Enzyme** node
- Select "Add Regulator" or "Add Input"
- Choose **Substrate**
- Set type: **Activation** (or "Positive" or "Required")
- This means: Enzyme needs Substrate to be active

#### Connection 2: Enzyme → Product (Production)

- Click **Product** node
- Add regulator: **Enzyme**
- Set type: **Activation**
- This means: Active Enzyme produces Product

#### Connection 3: Product → Enzyme (Inhibition - THE FEEDBACK!)

- Click **Enzyme** node again
- Add another regulator: **Product**
- Set type: **Inhibition** (or "Negative" or "Repression")
- This means: High Product levels shut down the Enzyme

**You just created a feedback loop!**

## Step 4: Define the Logic Rules (5 minutes)

Connections show "who affects whom." Logic rules specify "HOW they affect each other."

### For each node, we need to set its update rule:

#### Substrate (Input):

**Rule**: "Always ON" (we'll control this manually)

- Click **Substrate** node
- Look for "Properties" or "Logic" or "Update Rule"
- Set to: **External Input** (or "Manual Control")
- Initial state: **ON** (we're providing substrate)

**This means**: Substrate is available (the cell has molecules to convert)

#### Enzyme (The Critical Node):

**Rule**: "ON when Substrate is present AND Product is low"

- Click **Enzyme** node
- Open logic editor
- Set rule: **Substrate AND NOT Product**
- Initial state: **ON**

**What this means**:
- If Substrate is present AND Product is LOW → Enzyme works
- If Product is HIGH → Enzyme shuts down (feedback inhibition!)

#### Product (Output):

**Rule**: "Accumulates when Enzyme is active"

- Click **Product** node
- Set rule: **ON when Enzyme is ON**
- Initial state: **OFF** (no product at start)

**What this means**: Product builds up when the Enzyme is working.

### Quick check:

Your model should show:
- **Substrate** provides input
- **Enzyme** activates when Substrate is available and Product is low
- **Product** accumulates when Enzyme is active
- **Product** inhibits Enzyme (feedback loop)

**That's a functional biological network.**

## Step 5: Save Your Model (30 seconds)

Before we simulate, **save your work**.

- Look for "Save" button (usually top-right)
- Click it
- Your model is now saved in "My Models"

**You can come back to this anytime.**

## Step 6: Run Your First Simulation (3 minutes)

Time to see your model **come alive**.

### How to simulate:

1. Look for a **"Simulate"** button or tab
2. Click it

You'll see a **Simulation Controls** panel with options:
- **Number of steps** (iterations): Set to 25-50
- **Initial conditions**: Should default to what you set (Substrate = ON, Product = OFF)
- **Outputs to display**: Check boxes for Enzyme and Product (the components we care about)

### Run Baseline Simulation:

1. Click **"Run"** or **"Start Simulation"**
2. Watch a graph appear showing:
   - **X-axis**: Time (iterations)
   - **Y-axis**: Activity level (0 = OFF, 1 = ON)
   - **Lines**: One for each selected component

### What you should see:

**First few steps**:
- Enzyme starts ON (Substrate is available, Product is low)
- Product level rises (Enzyme is producing it)

**Middle steps**:
- Product continues to accumulate
- When Product reaches a threshold, Enzyme activity DROPS (feedback kicks in!)

**Later steps**:
- Enzyme activity drops to low levels
- Product stabilizes or plateaus

**You just witnessed feedback inhibition in action!**

**That rising-then-stabilizing curve is the hallmark of negative feedback control.**

## Step 7: Test a Perturbation (3 minutes)

Now let's **break** the model to understand how it works.

### Experiment: Knock Out the Feedback

**Question**: What happens if Product CAN'T inhibit the Enzyme?

**How to test this**:

1. Look for **"Perturbations"** or **"Interventions"** panel
2. Find the Product → Enzyme connection
3. **Remove the inhibition** OR **Set Product = OFF permanently**

**Method 1** (if available): Delete or disable the inhibition arrow

**Method 2** (universal): Knock out Product node
- Set Product to **"Knockout" (KO)** or **"Permanently OFF"**
- This simulates a mutation where Product can't be made

### Run the Perturbed Simulation:

1. Click "Run" again
2. Compare to your baseline graph

### What you should see:

Without feedback inhibition:
- Enzyme stays **ON continuously**
- Product (in a real system) would accumulate **indefinitely**
- The system has **lost control**

**In real biology**: This is what happens when regulatory pathways break (e.g., cancer cells lose growth control)

### Compare the graphs:

- **Baseline**: Product rises, then levels off (feedback works)
- **Knockout**: Product would keep rising (no feedback control)

**CER Moment**:
- **Claim**: "Feedback inhibition prevents overproduction"
- **Evidence**: "Baseline product stabilized at step 15. Knockout product continued rising."
- **Reasoning**: "Product normally inhibits the enzyme. Without that inhibition, the enzyme never shuts down, so product accumulates without limit."

**That's a real scientific argument. Based on a model you built.**

## Step 8: Export Your Data (1 minute)

You'll want this data for analysis or to show students.

### How to export:

1. Look for **"Download"** or **"Export"** button near the graph
2. Choose format:
   - **CSV** (for spreadsheets - recommended)
   - **PNG** (for screenshots)

3. Click "Export" or "Download"

### What you get:

**CSV file** with:
- Column 1: Iteration (time step)
- Column 2: Enzyme activity
- Column 3: Product activity

**You can now**:
- Open in Excel or Google Sheets
- Create your own charts
- Calculate metrics (time to plateau, peak product level, etc.)
- Use as data for student assessments

## Step 9: Celebrate (30 seconds)

**You just built a computational model.**

**In 20 minutes.**

**With no coding.**

**Your students can do this.**

## What You Built (And Why It Matters)

### You modeled a fundamental biological principle:

**Negative feedback control** - where the output of a pathway regulates its own production.

This shows up in:
- **Metabolism**: ATP inhibits glycolysis
- **Gene regulation**: Proteins repress their own genes
- **Endocrine systems**: Hormones regulate their own secretion
- **Immune response**: Cytokines downregulate immune activation

**One model. Dozens of applications.**

### You learned the modeling workflow:

1. **Identify components** (What's in the system?)
2. **Define relationships** (Who affects whom?)
3. **Encode logic** (HOW do they interact?)
4. **Simulate** (What does the system do?)
5. **Perturb** (What happens when we change something?)
6. **Analyze** (What does this tell us?)

**That's how scientists model biological systems.**

**That's what your students will do.**

### You created evidence for NGSS Practice 2:

✅ **Develop a model** - You built the network structure and logic
✅ **Use a model** - You ran simulations to predict behavior
✅ **Test with a model** - You knocked out feedback to test its role
✅ **Analyze model outputs** - You interpreted graphs and explained results

**That's NGSS Practice 2 in 20 minutes.**

## How to Use This Model with Students (3 Options)

### Option 1: Demo It (10 minutes)

**What to do**:
- Project your model
- Walk students through: "Here's Substrate, Enzyme, Product"
- Show the feedback arrow: "Product inhibits its own production"
- Run baseline: "See how Product levels off?"
- Run knockout: "Now watch what happens without feedback"

**Students learn**: Feedback inhibition concept through visual demonstration

**Best for**: Introducing the concept quickly

### Option 2: Students Explore It (20 minutes)

**What to do**:
- Share your model with students (view-only link)
- Give them 3 questions:
  1. "Describe what happens to Product over time in the baseline simulation"
  2. "Predict what will happen if we knock out the feedback"
  3. "Explain WHY feedback inhibition is important"
- Students run simulations and answer in a CER format

**Students learn**: How to interpret model outputs and make evidence-based arguments

**Best for**: Assessment or quick investigation

### Option 3: Students Build It (45-60 minutes)

**What to do**:
- Give students this guide (or your own simplified version)
- Have them build the model step-by-step
- Require: Screenshot of their model + simulation graph + CER paragraph

**Students learn**: Full modeling process from construction to analysis

**Best for**: Deep learning and hands-on practice

## The Questions You're Asking Right Now

### "That actually worked. But was it too simple?"

**No.**

Simple models are **powerful** models.

- They isolate core mechanisms
- They make assumptions explicit
- They're easier to test and revise

**Complex models come later.** Start simple. Build understanding. Then add complexity.

### "Can I use a different biological system?"

**Absolutely.**

Use this same workflow for:
- **Gene regulation** (repressor → gene → protein → repressor)
- **Predator-prey** (rabbits → foxes → rabbits)
- **Hormone feedback** (hormone → target → inhibitor → hormone)

**Same structure. Different components. Same learning.**

### "What if students get stuck?"

**That's the point.**

When students get stuck:
- They revise their logic
- They test alternatives
- They argue about causation

**That's inquiry-based learning.**

Your job: Ask guiding questions, don't give answers.

### "How do I grade this?"

**Rubric suggestion** (3 categories, 4 points each):

1. **Model Structure** (4 pts)
   - All components present?
   - Connections accurate?
   - Feedback loop identified?

2. **Simulation & Testing** (4 pts)
   - Baseline run completed?
   - Perturbation tested?
   - Results documented (screenshot/CSV)?

3. **Explanation** (4 pts)
   - CER paragraph present?
   - Evidence from simulation cited?
   - Reasoning connects mechanism to outcome?

**Total: 12 points**

**Time to grade: 2-3 minutes per student** (because the model and data speak for themselves)

## Your Challenge This Week: Build Model #2

You built the enzyme model. Now build a **different** one.

### Suggestions:

**Option A**: Gene regulation (lac operon)
- Components: LacI, Lactose, RNA Polymerase, mRNA
- Feedback: Lactose blocks LacI → RNA Polymerase activates → mRNA produced

**Option B**: Predator-prey dynamics
- Components: Rabbits (prey), Foxes (predator)
- Feedback: More rabbits → more foxes → fewer rabbits → fewer foxes

**Option C**: Glycolysis regulation
- Components: Glucose, PFK enzyme, ATP, F-1,6-BP
- Feedback: High ATP inhibits PFK → glycolysis slows

**Pick one. Build it. Test it.**

**Then decide which one you'll use with students next week.**

## What's Coming Next Week

**Week 8: From Molecules to Systems - "Multi-Scale Modeling (Or: How to Teach Everything at Once)"**

We're going **beyond single pathways** to show how models connect across scales:
- Molecular interactions → Cellular processes → Tissue responses → Organism behavior

How Cell Collective lets students explore:
- Signal transduction cascades
- Gene networks controlling development
- Metabolic integration across organelles

Plus: The mind-blowing moment when students realize **every biological scale is connected**.

---

## 🎯 Build Your Second Model

👉 **[Start Modeling at Cell Collective](https://cellcollective.org)**

👉 **[More Resources at Discovery Collective](https://discoverycollective.com)**

---

**Stop preparing to model someday. You just modeled today.**

**Now do it again. And again. Until it's second nature.**

**Let's do this.** 💪

---

## About the Authors

**Dr. Charles Martin** is an edtech entrepreneur focused on bringing computational modeling and systems thinking to K-12 education. He bridges cutting-edge university research with practical classroom applications.

**Dr. Marie Martin** brings 25+ years of educational leadership across K-12, higher education, government, and military sectors, specializing in curriculum development and instructional design.

Together, they co-founded Alexandria's Design to make systems modeling accessible to every classroom.
