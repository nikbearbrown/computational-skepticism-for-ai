# Hero Image Prompt Guide

Use this guide to create hero image prompt sheets for Humanitarians AI articles, Substack drafts, and book chapters.

This is an editorial art direction workflow, not a generic image prompt generator. The goal is to produce 3-5 usable text-to-image prompts that can become a hero image for an article or chapter.

## Output File Rule

For each article or chapter, create one Markdown prompt sheet.

Store it in the book/project `images/` directory, not in `drafts/`.

Filename:

```text
<article-or-chapter-base-name>-prompts.md
```

Examples:

```text
images/the-tool-that-talks-back-prompts.md
images/chapter-03-the-memory-that-stays-prompts.md
images/jobsekr-prompts.md
```

Use the article or chapter filename as the base when available. Remove only the extension and append `-prompts.md`.

## Standing Rule: Character Mandate

Every hero image prompt must include a central character.

The character does not have to be human, but it must function as the protagonist of the image: a figure the reader can project onto, feel tension through, or be unsettled by.

Acceptable character types:

- archetype: the student, the researcher, the applicant, the teacher, the analyst
- symbolic historical figure: era-specific silhouette or posture, not a photorealistic likeness
- fictional construct: robot, automaton, golem, paper figure, shadow figure
- non-human entity with posture: a machine waiting at a desk, a bird at a chalkboard, a laboratory notebook standing upright
- mythic or allegorical figure: guide, witness, messenger, gatekeeper

Unacceptable:

- product shot with no character
- abstract background with no protagonist
- still life with no implied narrative
- dashboard/screen mockup as the whole image
- generic AI robot staring at the viewer

The character can be small, back-facing, silhouetted, obscured, or off-center. But it must carry the emotional weight.

## Input Needed

Use the article or chapter text as source material.

If source is thin, use the title, subtitle, front matter, and first 3-5 paragraphs. Do not invent facts. Build the image around the actual claim, not a generic theme.

## Phase 0: Thematic Extraction

Before writing image prompts, extract:

### Core Message

One sentence naming what the article or chapter is really arguing.

Example:

> A stale job listing is not harmless; it steals time from international students who are already living under a legal countdown.

### Concept Type

Choose one:

- Attribute: image shares qualities with the subject, such as fragility, scale, weight, pressure, opacity
- Structure: image shows hierarchy, maze, gate, classroom, archive, system, chain, map
- Process: image implies movement, transformation, countdown, discovery, decay, repair

### Emotional Register

Name the tone:

- urgent
- contemplative
- unsettling
- precise
- humane
- lonely
- defiant
- mournful
- optimistic
- provocative

### Character Candidates

List three possible central characters.

Use this table:

```md
| Candidate | Type | Why This Character Fits |
|---|---|---|
| Option 1 | archetype / construct / non-human / historical-symbolic | ... |
| Option 2 | ... | ... |
| Option 3 | ... | ... |
```

Then select one and justify it in one sentence.

Ask: would a reader pause for this figure before reading the headline?

### Environment Metaphors

List three possible environments or situations the character could inhabit.

Draw from:

- architecture: hallway, archive, classroom, laboratory, terminal, courthouse, factory
- nature: storm, field, river, forest path, cliff edge, roots
- objects: notebook, door, clock, ladder, map, machine, table, filing cabinet
- body: pulse, nervous system, skeleton, breath, scar tissue
- geometry: maze, grid, broken circle, branching graph, funnel

The character plus environment should make the image's argument.

## Prompt Requirements

Every prompt must:

- be text-to-image ready
- include the central character first
- include the environment second
- include style, composition, palette, lighting, and aspect ratio
- state that the image has absolutely no text
- avoid photorealistic likenesses of real people
- avoid copyrighted characters
- avoid generic AI imagery
- avoid bokeh blobs, decorative gradients, neon tech fog, and meaningless robots

Every prompt must include:

```text
--no text, letters, words, numbers, labels, signs, captions, annotations, watermarks, typography, glyphs
```

For Midjourney-style prompts, use:

```text
--v 7 --style raw --stylize 75 --ar 16:9
```

For non-Midjourney tools, write a structural prompt in full sentences.

## Recommended Prompt Set

Create 3-5 prompts per article or chapter.

Minimum set:

1. Safe / Proven
2. Editorial Stretch
3. Cover-Worthy

Optional additions:

4. Minimal / Brutalist
5. Human / Documentary

Each prompt should use a different character type or a meaningfully different character posture. Do not make five color variations of the same image.

## Prompt Format

For each prompt, use this structure:

```md
## Prompt 1: Safe / Proven

**Character:** ...

**Environment:** ...

**Mood:** ...

**Best for:** ...

**Prompt:**
...

**Why it works:**
...
```

## Image Style Defaults

Use editorial hero image language:

- full-bleed magazine hero image
- clean editorial illustration
- restrained symbolic realism
- matte textures
- high-contrast but not glossy
- strong negative space for headline overlay
- character visible in desktop and mobile crops

Preferred palettes:

- soot black, warm white, dried red
- charcoal, ledger tan, surgical blue
- off-white, graphite, muted gold
- deep brown, cream, institutional green
- black, white, one sharp accent color

Avoid one-note purple/blue gradients unless the source specifically demands them.

## Lighting Options

Choose one per prompt and explain why.

- Soft editorial diffused: humane, reflective, cultural
- High-contrast studio: power, pressure, systems, judgment
- Overcast flat: ambiguity, grief, complexity
- Candle / single source: introspection, history, isolation
- Cold fluorescent: institutions, bureaucracy, labs, classrooms
- Morning side light: possibility, repair, beginning again

Lighting must interact with the character, not just the background.

## Crop and Export Notes

Design primarily for:

```text
16:9, 1920x1080
```

Also note whether the image will survive:

- 3:2 article header
- 4:5 social crop
- 9:16 story crop

The character must remain visible in every crop.

Leave a safe zone for headline typography. Do not place the character's face or primary gesture where the title will sit.

## Ethics and Compliance

Before approving prompts, check:

- no real identifiable person is depicted without consent
- historical figures are symbolic, not portrait likenesses
- no culturally loaded symbols used carelessly
- no embedded text in the image
- no copyrighted character imitation
- no stereotype carried by the character choice
- no robot/non-human character that reads as dehumanizing by proxy
- image can be labeled AI-generated if publication policy requires it

## Output Template

Use this template for each generated prompt sheet:

```md
# Hero Image Prompts: [Article or Chapter Title]

Source file: `[source filename]`
Output target: `images/[source-base]-prompts.md`

## Thematic Extraction

**Core message:** ...

**Concept type:** Attribute / Structure / Process

**Emotional register:** ...

## Character Selection

| Candidate | Type | Why This Character Fits |
|---|---|---|
| Option 1 | ... | ... |
| Option 2 | ... | ... |
| Option 3 | ... | ... |

**Selected character:** ...

**Reason:** ...

## Environment Metaphors

1. ...
2. ...
3. ...

## Prompt 1: Safe / Proven

**Character:** ...

**Environment:** ...

**Mood:** ...

**Best for:** ...

**Prompt:**
...

**Why it works:**
...

## Prompt 2: Editorial Stretch

**Character:** ...

**Environment:** ...

**Mood:** ...

**Best for:** ...

**Prompt:**
...

**Why it works:**
...

## Prompt 3: Cover-Worthy

**Character:** ...

**Environment:** ...

**Mood:** ...

**Best for:** ...

**Prompt:**
...

**Why it works:**
...

## Optional Prompt 4: Minimal / Brutalist

**Prompt:**
...

## Optional Prompt 5: Human / Documentary

**Prompt:**
...

## Crop Notes

- Desktop 16:9:
- Article 3:2:
- Social 4:5:
- Story 9:16:
- Headline safe zone:

## Ethics Checklist

- [ ] central character present
- [ ] no embedded text
- [ ] no identifiable real person
- [ ] no careless cultural symbolism
- [ ] no copyrighted character imitation
- [ ] character survives mobile crop
- [ ] prompt avoids generic AI imagery
```

## Example Prompt

```text
A lone international student seen from behind, small in the right third of the frame, standing before a hallway of closed institutional doors, one door faintly outlined by morning side light, scattered application papers at their feet with no readable markings, restrained editorial realism, matte textures, warm white walls, charcoal shadows, dried red accent on a single thread tied around the student's wrist, strong negative space in upper left for headline overlay, full-bleed magazine hero image --v 7 --style raw --stylize 75 --ar 16:9 --no text, letters, words, numbers, labels, signs, captions, annotations, watermarks, typography, glyphs, neon, bokeh, glossy plastic, photorealistic portrait, face visible
```

