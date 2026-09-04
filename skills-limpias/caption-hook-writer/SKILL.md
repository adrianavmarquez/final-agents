---
name: caption-hook-writer
description: >
  Writes caption hooks for any brand, persona, format, and awareness level using the Odyssey hook
  framework. Always references the hook database and hook research brief as inputs. Use this skill
  whenever Jake or the team needs to: write caption hooks, generate on-screen text for ads,
  build a hook set for a brief, run a hook writing session, produce caption variants across formats
  or awareness levels, or pivot hooks across personas, motivators, or benefits.
  Trigger on: "write caption hooks", "give me captions for [persona/format]", "write hooks for [brand]",
  "generate hook options", "pivot these hooks to [different persona/motivator/benefit/awareness level]",
  "run a hook writing session", or any request to produce on-screen text for an ad.
  Always load the hook database PDFs and a completed Hook Research Brief before running this skill.
  Never write captions without strategic inputs locked in first.
---

> **Capa 0.** Antes de escribir, carga `marca-reglas-duras`. Sus siete reglas y su léxico mandan sobre cualquier instrucción de esta skill.

# Caption Hook Writer

Caption hooks are the on-screen text overlays that stop the scroll before a word is spoken. They are the highest-priority hook component, they must work on mute, they must speak to exactly one person, and they must be oddly specific.

This skill writes caption hooks using locked strategic inputs: persona, motivator, benefit, format, and awareness level. It references the hook database for category selection and the Hook Research Brief for language and specificity.

---

## Step 0. Check Project Files First

Before writing any hooks, always check the project files for this brand. Project files contain the brand's persona map, creative strategy, past briefs, hook research briefs, and any prior hook sets already written.

**Do this before anything else:**
1. Review all available project files for the brand
2. Identify any existing Hook Research Briefs for the target persona, use the motivators, desired outcomes, and hook-ready language already documented there
3. Check whether any hook sets have already been written for this persona + format + awareness level combination, avoid duplicating what already exists
4. Note any creative directions, angles, or formats the brand has already tested, flag if the requested hooks would repeat existing work

If a Hook Research Brief exists in the project files for this persona, use it as the primary source for motivators, benefit angles, and hook-ready language. Do not ask the user to re-input information that is already documented.

---

## Required Inputs Before Writing

Never generate captions without all five inputs confirmed. If any are missing, ask before proceeding.

| Input | What it is | Where it comes from |
|---|---|---|
| **Persona** | The specific micropersona this is for | Brand persona map |
| **Motivator** | The one emotional truth the hook taps | Hook Research Brief |
| **Benefit** | The outcome the persona cares about | Hook Research Brief |
| **Format** | The ad format being briefed | Creative brief or session |
| **Awareness level** | TOF / MOF / BOF | Brief or session context |

---

## The Caption Hook Golden Rules

1. **Oddly specific beats vague every time.** `"$94/month"` beats `"save money"`. `"6 years"` beats `"a long time"`. Numbers, real timeframes, and exact situations are what make the right person stop.

2. **Under 10 words when possible.** Under 7 is ideal. One idea per caption. Never combine two hooks into one.

3. **Name the persona or their situation, not the product.** The caption should make the target viewer feel called out. The wrong viewer should feel nothing.

4. **Caption and visual action must complement, not repeat.** If the visual shows the problem, the caption names the feeling. If the visual shows the feeling, the caption names the proof.

5. **Caption and voiceover must complement, not duplicate.** If the caption says the number, the VO names the emotion. If the caption names the emotion, the VO says the number.

6. **Vary hook types across a set.** Never write 5 captions of the same type. Across a set of 5+: aim for at least 3 different caption hook categories.

---

## Caption Hook Categories. Quick Reference

Load `hook-database-SKILL.pdf` and `caption-hooks.pdf` for full templates. Categories:

| # | Category | Best awareness level |
|---|---|---|
| 1 | POV Scenarios | TOF / MOF |
| 2 | Question Hooks | TOF / MOF |
| 3 | Gifting Hooks | MOF / BOF |
| 4 | Authority Building | MOF / BOF |
| 5 | Social Proof | MOF / BOF |
| 6 | PSA / Announcement | TOF |
| 7 | Urgency / Time-Sensitive | BOF |
| 8 | Shock / Surprise | TOF |
| 9 | Numbers / Statistics | TOF / MOF |
| 10 | Scenario / Story | TOF / MOF |
| 11 | Surprise Reveals | TOF / MOF |
| 12 | Benefit Showcase | MOF / BOF |
| 13 | Problem Identification | TOF |
| 14 | Routine Showcase | MOF |
| 15 | Sales & Promotion | BOF |
| 16 | Enemy | TOF |

---

## Format → Caption Guidance

Different formats demand different caption energy. Match before writing.

| Format | Caption notes |
|---|---|
| **Street Interview** | Caption often names the question asked or frames the exchange. Short and direct. |
| **Podcast / Two-Person** | Caption teases the insight or frames the debate. Can be slightly longer. |
| **Staged Organic Moment** | Caption feels like an overheard thought. POV and scenario structures work well. |
| **Talking Head / UGC** | Caption matches conversational energy, fragments and short punches. |
| **Before / After** | Caption states the contrast directly: "Before: $X. After: $X." |
| **Text / Overlay** | Caption IS the ad, carries full narrative weight. Can use multi-line reveal structure. |
| **TikTok Native** | Caption feels native. POV, question, or scenario. Never sounds like an ad. |
| **In-Car** | Short, punchy, conversational. Matches the intimate feel of the format. |
| **Product Demo** | Caption frames what the viewer is about to see. Numbers and proof structures. |
| **ASMR / Pattern Interrupt** | Caption can lean unexpected: "Hear me out" or "This is going to sound weird but" |

---

## Output Format

For every caption hook session, output in this structure:

---

**PERSONA:** [Name]
**MOTIVATOR:** [One sentence]
**BENEFIT:** [One sentence]
**FORMAT:** [Format name]
**AWARENESS LEVEL:** [TOF / MOF / BOF]

---

**Hook 1**
- **Caption:** [The caption, under 10 words ideally]
- **Category:** [Which of the 16 caption hook categories]
- **Visual action:** [What the creator is doing on screen. 1 sentence]
- **Voiceover:** [First spoken words. 1. 2 sentences]
- **Why it works:** [One sentence on why this combination stops this specific persona]

**Hook 2**
[Same structure]

[Continue for all hooks in the set]

---

## Pivot Workflows

Once a hook set is written, pivots are the fastest way to expand the creative library. Run these in sequence:

### Awareness Pivot
Keep persona + motivator + benefit + format. Change awareness level only.
- TOF set → write BOF versions of the same hooks
- Watch how the caption's job changes: TOF introduces the problem, BOF removes the last objection

### Benefit Pivot
Keep persona + motivator + format + awareness level. Change benefit angle only.
- Same motivator expressed through 3 different benefits = 3 completely different hook sets
- Pull benefit options from the Hook Research Brief desired outcomes section

### Motivator Pivot
Keep persona + format + awareness level. Change motivator entirely.
- Same persona, different emotional truth = different person stopping
- Pull motivator options from the Hook Research Brief motivators section

### Persona Pivot
Keep format + awareness level. Change persona entirely.
- Same formats, completely different hooks
- Run a new Hook Research Brief for the new persona before pivoting

### Format Pivot
Keep persona + motivator + benefit + awareness level. Change format only.
- Same strategy, different creative execution
- Caption energy and structure will shift significantly, see Format → Caption Guidance above

---

## Quality Check. Before Finalizing Any Caption

Run this check on every caption before including it in output:

- [ ] Is it under 10 words?
- [ ] Does it contain a specific number, timeframe, or situation, not a vague adjective?
- [ ] Does it name the persona's situation, not the product?
- [ ] Is it a different hook category from the others in the set?
- [ ] Would the wrong persona feel nothing reading this?
- [ ] Does it complement the visual action and voiceover without duplicating them?

If any box is unchecked, rewrite before delivering.

---

## Reference Files

- `references/caption-pivot-examples.md`. Worked examples of full pivot sequences showing how one strategic foundation expands into a full creative matrix
