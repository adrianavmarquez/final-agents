---
name: prompt-builder
description: Generates a perfectly structured JSON prompt for any AI-assisted design task (ads, social posts, decks, mockups, illustrations, layouts, etc.). Use this skill whenever Adri asks to generate a design prompt, build a prompt for AI image generation, create a visual concept prompt, or says anything like "let's build a prompt for," "give me a prompt for," "I want to generate [design thing]," or "help me prompt [design task]." Also trigger when Adri uploads a brand file or brief and says she wants to create something. This skill runs a structured intake form and outputs a complete, filled-in JSON prompt ready to paste into any AI design tool.
---

> **Capa 0.** Antes de escribir, carga `marca-reglas-duras`. Sus siete reglas y su léxico mandan sobre cualquier instrucción de esta skill.

# Prompt Builder

A structured intake skill that asks the right questions and outputs a complete JSON prompt for any AI-assisted design task. It uses brand files already uploaded to the project as the source of truth for visual identity, tone, and aesthetics, so Adri never has to re-explain the brand.

---

## How this skill works

1. **Read brand context first**, before asking anything, scan project files for brand briefs, guidelines, spec sheets, or research docs. Extract: brand name, fonts, colors, tone, imagery style, persona. This becomes the default layer. If no files are found, note it and proceed.
2. **Run the intake form**, present all questions at once, numbered, organized into sections. Adri fills in what she knows and skips what doesn't apply.
3. **Generate the JSON prompt**, synthesize her answers + brand context into a complete, filled-in JSON prompt ready to use.

---

## Step 1: Read brand context from project files

Before presenting the intake form, silently scan for any uploaded files in the project. Look for:
- Brand guidelines, spec sheets, or style guides
- Brand research briefs (brand_identity, visual_system, target_audience fields)
- Mood boards, creative briefs, or campaign docs
- Any previously built brand context document

Extract and hold in memory:
```
brand_name, tagline, primary_font, secondary_font, primary_color_hex, 
secondary_color_hex, accent_color_hex, background_preference, imagery_style, 
tone_adjectives, persona_summary, logo_treatment
```

Pre-fill these as defaults in the JSON output. If a field is explicitly answered in the intake, override the default. If not answered and not in brand files, mark as `"[DEFINE]"`.

---

## Step 2: Run the intake form

Present this exact structure. Label it clearly as a form. Tell Adri to answer what she knows and skip what doesn't apply (just write "skip" or leave blank).

---

### PROMPT BUILDER. Intake Form

> Brand context has been loaded from your project files. Answer only what's specific to this piece. Skip anything that doesn't apply.

---

**SECTION 1. THE PIECE**

1. What are we making? *(e.g., Instagram post, static ad, email header, deck slide, product mockup, illustration, logo lockup, carousel, story, banner)*
2. What is the goal of this design? *(e.g., drive clicks, announce a launch, build desire, explain a feature, grow followers)*
3. Who is this talking to? *(Describe the person seeing this, be specific. Age, mindset, moment they're in)*

---

**SECTION 2. THE MESSAGE**

4. What is the main headline or message? *(The single most important thing this design says)*
5. Is there a subheading or secondary message? *(Optional. Must add something new, not repeat the headline)*
6. Is there body copy? *(Optional. Short supporting text. 1-3 sentences max)*
7. Is there a CTA? *(Optional. What action do you want them to take? e.g., "Shop Now," "Learn More," "DM us")*

---

**SECTION 3. THE VISUAL**

8. What is the visual hero? *(What should the eye land on first? e.g., product, person, typographic statement, scene, illustration)*
9. What elements do you want included? *(List anything specific: product photo, model, background scene, prop, texture, pattern, icon, badge, etc.)*
10. What should the composition feel like? *(e.g., centered and minimal, editorial with tension, full-bleed lifestyle, flat lay, tight crop, dynamic angle)*
11. What is the background? *(e.g., solid brand color, white, dark, textured, lifestyle scene, gradient, transparent)*
12. What lighting or mood? *(e.g., soft natural light, studio clean, golden hour, moody and dramatic, bright and airy)*

---

**SECTION 4. STYLE AND ENERGY**

13. What graphic design style? *(e.g., editorial, minimal, maximalist, brutalist, organic, luxury, playful, clean commercial, handcrafted)*
14. What is the sentiment or emotional tone? *(e.g., confident, romantic, urgent, warm, aspirational, rebellious, joyful, serene)*
15. Are there any variation vectors? *(Optional. Things you want explored in different versions, e.g., two color options, two headline positions, product vs. lifestyle version)*

---

**SECTION 5. TECHNICAL**

16. What is the aspect ratio or format? *(e.g., 1:1 square, 4:5 portrait, 9:16 story, 16:9 landscape, custom dimensions)*
17. What platform or output is this for? *(e.g., Instagram feed, Meta ads, Pinterest, email, print, deck)*
18. Any must-avoid or off-limits? *(Anything that would feel wrong, words, visuals, colors, styles, references)*

---

## Step 3: Generate the JSON prompt

After receiving answers, synthesize everything into this structure. Every field must be filled in or marked `"[DEFINE]"`, never leave fields empty or generic.

```json
{
  "prompt_meta": {
    "design_task": "",
    "platform": "",
    "aspect_ratio": "",
    "goal": "",
    "persona": ""
  },
  "brand_context": {
    "brand_name": "",
    "primary_font": "",
    "secondary_font": "",
    "primary_color": "",
    "secondary_color": "",
    "accent_color": "",
    "logo_treatment": "",
    "tone": []
  },
  "copy": {
    "headline": "",
    "subhead": "",
    "body": "",
    "cta": ""
  },
  "visual_direction": {
    "visual_hero": "",
    "elements": [],
    "composition": "",
    "background": "",
    "lighting": "",
    "imagery_style": ""
  },
  "style": {
    "graphic_design_style": "",
    "sentiment": "",
    "energy": ""
  },
  "typography": {
    "headline_font": "",
    "headline_weight": "",
    "headline_color": "",
    "subhead_font": "",
    "body_font": "",
    "hierarchy_notes": ""
  },
  "technical": {
    "safe_zones": "",
    "format_notes": ""
  },
  "variations": [],
  "must_avoid": [],
  "full_image_generation_prompt": ""
}
```

### The `full_image_generation_prompt` field

This is the most important field. After filling in all structured fields, write a single, continuous, richly detailed paragraph that synthesizes everything into a ready-to-paste prompt for an AI image generation tool (Midjourney, Firefly, DALL-E, Ideogram, etc.).

It must follow this structure:

```
Create a [design task] for [brand name]. [Aspect ratio].

COMPOSITION: [What's in the frame, where, how it's arranged. Visual hero. Hierarchy. What the eye does first.]

COPY: Render "[headline]" as the dominant text element in [position]. [Subhead and CTA instructions if applicable.]

TYPOGRAPHY: [Font, weight, size relationship, color, placement rules from brand context.]

COLOR AND TREATMENT: [Background, color palette, contrast requirements, any textures or overlays.]

LIGHTING: [Lighting direction, quality, mood contribution.]

STYLE: [Graphic design style. Aesthetic category. Mood. Energy.]

BRAND IDENTITY: [Logo placement if applicable. Brand cues that must be present.]

MUST AVOID: [Anything off-limits.]

MOOD: [One sentence closing statement on the overall emotional feeling this piece should create.]
```

---

## Output rules

- Never use em dashes. Use periods, commas, or colons instead.
- Never add fields that weren't asked for or aren't in brand context.
- `variations` is an array of strings, each describing a distinct version to explore.
- `elements` is an array of specific visual items to include.
- `must_avoid` is an array of anything explicitly excluded.
- The JSON must be valid and copyable.
- After outputting the JSON, offer to refine any single field or rewrite the `full_image_generation_prompt` for a specific tool (Midjourney, Firefly, Ideogram).
