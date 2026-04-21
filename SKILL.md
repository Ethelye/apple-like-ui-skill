---
name: apple-like-ui
description: Design, implement, or audit Apple Human Interface Guidelines-inspired user interfaces for web, desktop, mobile, and native apps. Use when Codex needs to make a UI feel Apple-like, iOS-like, macOS-like, visionOS-like, refined, platform-native, spacious, legible, accessible, responsive, or aligned with Apple-style layout, typography, color, materials, motion, icons, controls, navigation, or UX writing. Also use when refactoring an existing UI toward Apple-like polish while avoiding direct Apple trademark or app UI cloning.
---

# Apple-like UI

Create interfaces that feel at home in the Apple ecosystem: content-first, calm, legible, adaptive, precise, and respectful of accessibility settings.
Use Apple HIG as a design-quality reference, not as permission to clone Apple apps, Apple trademarks, proprietary assets, product imagery, or confidential design work.
Translate the principles into the user's product, codebase, and platform instead of forcing a generic "Apple skin" onto every problem.

## First Moves

1. Identify the target surface: iOS, iPadOS, macOS, watchOS, tvOS, visionOS, responsive web, Electron, desktop web app, or native app.
2. If unspecified, default to responsive web with Apple-inspired interaction, visual hierarchy, and accessibility behavior.
3. Read `references/apple-hig-synthesis.md` before making design decisions.
4. For component-specific work, use `references/apple-hig-source-index.md` to locate relevant official HIG pages.
5. Prefer the project's existing design system, framework, components, tokens, and icon library.
6. Add dependencies only when the user explicitly requests them or the repo already depends on them.
7. Build the actual product surface first; avoid landing-page filler unless the user asks for a marketing page.
8. Verify visually and functionally before claiming the interface is polished.

## Reference Corpus

- `references/apple-hig-synthesis.md`: distilled guidance from the downloaded Apple HIG corpus. Load this first.
- `references/apple-hig-source-index.md`: source map of the 174 official HIG pages collected from Apple Developer.
- `scripts/collect_apple_hig.py`: Python collector for refreshing the corpus from Apple's official JSON endpoints.

Run the refresh script from the skill folder or from a workspace:

```bash
python scripts/collect_apple_hig.py --out apple_hig_corpus
```

Use refreshed corpus files as source material for your own concise synthesis.
Do not paste large chunks of Apple documentation into responses, source files, or generated app copy.
When a rule seems platform-specific or recently changed, refresh or inspect the source corpus before making a strong claim.

## Design Stance

- Make content the hero; controls and navigation support the work without competing for attention.
- Remove visual noise before adding effects, translucency, animation, or decorative polish.
- Use hierarchy through spacing, alignment, weight, semantic color, and progressive disclosure.
- Keep the interface calm: fewer competing accents, fewer surfaces, fewer ornamental shapes.
- Make primary workflows obvious and secondary actions discoverable.
- Prefer familiar platform patterns over custom interaction inventions.
- Treat accessibility, localization, and adaptation as core polish, not cleanup.
- Preserve the app's own brand and subject matter; Apple-like does not mean sterile or identical.
- Use measured delight only where it improves feedback, comprehension, or confidence.
- Keep decisions reversible and local to the UI layer unless the user asks for broader architecture work.

## Layout

- Group related items with spacing, alignment, subtle separators, background shapes, or material layers.
- Give essential information enough room and put it near the top and leading side in the current reading direction.
- Use progressive disclosure for secondary details, filters, advanced settings, and destructive controls.
- Extend content to screen or window edges when appropriate, while keeping controls inside safe areas and readable margins.
- Avoid crowding controls around content; let whitespace clarify relationships.
- Align edges, baselines, icons, and values so the eye can scan without friction.
- Keep repeated rows dense enough for work, but not so dense that targets become hard to activate.
- Respect safe areas, notches, home indicators, title bars, toolbars, sidebars, and resizable windows.
- Support orientation changes, split views, external displays, browser zoom, and small/mobile widths.
- Avoid sudden layout swaps; keep responsive changes stable until the current layout truly stops fitting.

## Visual Hierarchy

- Use one clear top-level title or focal content region per view.
- Reserve hero-scale type for true hero surfaces, not compact panels or controls.
- Use size, weight, grouping, and position before using bright color for hierarchy.
- Use separators lightly; prefer spacing first, then subtle rules or background grouping.
- Make selected, focused, and active states visually distinct without overwhelming nearby content.
- Keep background layers quieter than foreground controls and content.
- Show enough of offscreen or hidden content to imply scrollability when helpful.
- Use sidebars, tab bars, segmented controls, and toolbars according to task structure, not decoration.
- In data-heavy tools, prioritize scanning, comparison, and repeated action over editorial drama.
- In media or immersive tools, let the media breathe and keep controls available but restrained.

## Color

- Use semantic colors rather than one-off hard-coded values.
- On web, define tokens like `--bg`, `--bg-elevated`, `--text`, `--text-secondary`, `--separator`, `--accent`, `--control-bg`, and `--material-bg`.
- Redefine semantic tokens for dark mode and high-contrast contexts.
- Use system/native colors in SwiftUI, UIKit, AppKit, and platform frameworks when available.
- Keep accent color meaningful: primary actions, selection, status, progress, and links.
- Avoid using the same color to mean different things in the same workflow.
- Never rely on color alone to communicate status, validation, selection, or interactivity.
- Pair color with labels, icons, shapes, position, or pattern.
- Test colorful content beneath translucent controls for contrast and legibility.
- Use wide-gamut or saturated color carefully; vivid color can become visually loud on modern displays.

## Dark Mode

- Respect the user's system appearance choice when the platform supports it.
- Avoid app-specific light/dark toggles unless the product has a strong reason.
- Ensure text, icons, separators, charts, empty states, and illustrations work in both modes.
- Use adaptive background layers to preserve depth instead of inverting colors mechanically.
- Avoid pure white surfaces glowing inside dark interfaces.
- Avoid low-contrast dark text on dark materials when Increase Contrast or Reduce Transparency changes are active.
- Provide separate image assets only when one asset cannot remain clear in both appearances.
- Prefer semantic label colors for text hierarchy.
- Keep shadows subtle in dark mode; use elevation, borders, or material contrast when shadows disappear.
- Check dark-mode forms and alerts with error, disabled, and focus states.

## Materials

- Use material to clarify hierarchy between foreground controls and background content.
- Use glass-like effects mainly for navigation, toolbars, tab bars, sidebars, floating controls, sheets, and popovers.
- Do not use glass as a general content-card decoration.
- Keep content layers readable, stable, and grounded.
- Choose material by semantic purpose and legibility, not by apparent color.
- Add dimming, blur, opacity, or stronger background fill when rich content makes labels hard to read.
- Provide opaque fallbacks for browsers or devices without `backdrop-filter`.
- Avoid stacking multiple translucent surfaces unless the hierarchy remains obvious.
- Keep glass controls sparse; too much blur makes the UI feel busy and fragile.
- Treat Liquid Glass-inspired styling as a functional layer, not a wallpaper effect.

## Typography

- Use system fonts where possible.
- On web, start with `-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Arial, sans-serif`.
- Use a small, intentional type scale for title, heading, body, secondary, caption, and code roles.
- Prefer Regular, Medium, Semibold, and Bold weights.
- Avoid ultralight and thin weights except for large decorative text that remains legible.
- Keep typefaces minimal; mixing many faces weakens hierarchy and polish.
- Support Dynamic Type, browser zoom, and larger accessibility text sizes.
- At large text sizes, stack metadata, reduce columns, and avoid useful text truncation.
- Match icon stroke or symbol weight to adjacent text weight.
- Avoid negative letter spacing and viewport-scaled font sizes.

## Controls

- Use standard components when available because they include familiar states and accessibility behavior.
- Buttons need a hit region of at least 44x44 pt or CSS px equivalent.
- Use larger targets for spatial, TV, watch, or gesture-heavy interfaces.
- Custom controls need visible hover, active, pressed, focus-visible, disabled, selected, loading, and error states where relevant.
- Use a prominent style for the most likely action, usually one primary action per view.
- Keep prominent actions to one or two per surface.
- Distinguish the preferred action by style, not by making peer buttons different sizes.
- Never give destructive actions the strongest primary treatment.
- Pair destructive actions with clear copy and confirmation when recovery is hard.
- Prefer icon-only controls only when the icon is familiar and has an accessible label or tooltip.

## Components

- Use tab bars for peer destinations that people switch between frequently.
- Use sidebars for larger navigation structures, persistent collections, or document-style apps.
- Use segmented controls for small mutually exclusive modes, not broad navigation trees.
- Use menus for secondary commands, sorting, filtering, and less frequent actions.
- Use sheets for focused tasks that keep context visible.
- Use popovers for lightweight contextual choices.
- Use alerts sparingly for blocking decisions, destructive confirmation, or critical information.
- Use search fields with clear placeholder text, tokens, scope controls, or filters only when the task benefits.
- Use lists and tables when scanning and repeated action matter more than visual storytelling.
- Use cards only for repeated items or contained tools; avoid nested cards and decorative card stacks.

## Icons and Symbols

- Icons should express one concept with a simple, recognizable shape.
- Prefer SF Symbols in native Apple apps.
- On web, use the project's existing simple icon set and tune stroke width to text weight.
- Keep icon size, weight, detail, perspective, and optical alignment consistent.
- Use fill variants for selected or high-emphasis states when the icon family supports it.
- Use outline variants for toolbars, lists, and lower-emphasis commands.
- Provide accessible labels for icon-only buttons and custom icons.
- Avoid text inside icons unless essential; localize or mirror it when needed.
- Avoid replicas of Apple hardware, Apple logos, and Apple trademarks.
- Do not use SF Symbols or confusingly similar symbols in app icons, logos, or trademark-like marks.

## Motion

- Add motion only for feedback, continuity, state change, progress, or orientation.
- Keep feedback animations brief, precise, and interruptible.
- Avoid extra animation on actions people perform repeatedly.
- Never make animation the only way to understand a change.
- Respect `prefers-reduced-motion` and platform Reduce Motion settings.
- Replace large movement, zoom, parallax, blur animation, and repeated bounce with simpler fades or instant state changes.
- Use transitions that match physical expectation: a panel that slides in from one edge should exit coherently.
- Avoid slow entrance animations that delay work.
- Use symbol or icon animation only when it clarifies state or confirms action.
- In spatial-style UI, avoid peripheral motion, world rotation, sustained oscillation, and head-locked content.

## Accessibility

- Design for perceivable, intuitive, and adaptable interaction.
- Meet at least WCAG AA contrast expectations: 4.5:1 for normal text and 3:1 for large or bold text.
- Provide keyboard navigation, screen-reader labels, focus order, visible focus indicators, and gesture alternatives.
- Ensure forms have labels, hints, validation text, and errors near the relevant field.
- Keep controls large enough and spaced enough to prevent accidental activation.
- Offer alternatives to audio-only cues, color-only cues, time-limited dismissals, and complex gestures.
- Avoid autoplaying media without clear controls.
- Reduce flashing, fast motion, and blinking effects.
- Support right-to-left layout, localization length changes, and culturally inclusive imagery.
- Test with zoomed text and narrow widths; Apple-like polish collapses quickly when text clips.

## Writing

- Use plain language and remove words that do not help people act or understand.
- Label actions with verbs such as `Send`, `Add`, `Continue`, `Save`, `Cancel`, and `Done`.
- Match tone to context: direct for serious flows, warmer for celebratory moments.
- Keep terminology consistent across the product.
- Empty states should explain what happened and offer a useful next action.
- Error messages should be blame-free, specific, and placed near the problem.
- Avoid cute labels when clarity matters.
- Avoid vague links like `Click here`; name the destination or action.
- Use device-appropriate verbs: tap for touch, click for pointer, press when platform convention calls for it.
- Write settings labels for the enabled state and let people infer the disabled state.

## Platform Lenses

- iOS: prioritize the main task, limit chrome, support orientation and Dynamic Type, and place common actions where thumbs can reach.
- iPadOS: design for resizing, multitasking, keyboard/pointer use, sidebars, split views, and adaptable navigation.
- macOS: respect window behavior, toolbars, sidebars, menus, pointer hover, keyboard shortcuts, and document workflows.
- watchOS: keep views glanceable, focused, edge-to-edge, and careful with side-by-side controls.
- tvOS: design for focus, distance viewing, large text, remote input, safe areas, and subtle scale feedback.
- visionOS: prioritize comfort, depth restraint, gaze-friendly controls, stable windows, and materials that keep people grounded.
- Web: translate the principles with semantic HTML, responsive CSS, accessible states, and restrained material effects.
- Electron or desktop web: combine web implementation with desktop expectations for menus, keyboard shortcuts, resizable panes, and window chrome.

## Web Implementation Defaults

- Use semantic HTML before custom widgets.
- Use CSS variables for all color, spacing, radius, shadow, material, and motion tokens.
- Use a 4px spacing grid with generous section spacing and tighter repeated-row spacing.
- Use restrained radii: 8-12px for compact controls and 14-20px for larger surfaces when appropriate.
- Avoid making every element pill-shaped.
- Use `backdrop-filter` only for functional layers with legibility fallbacks.
- Provide `:hover`, `:active`, `:focus-visible`, `[aria-selected]`, `[aria-expanded]`, disabled, loading, and error styles.
- Respect `prefers-color-scheme`, `prefers-reduced-motion`, and high-contrast or forced-colors modes where possible.
- Use container queries, fluid grids, and stable dimensions for controls, boards, media, and toolbars.
- Test at mobile, tablet, and desktop widths before finishing.

## Implementation Pass

1. Inventory the current UI: layout, tokens, components, states, copy, icons, motion, and accessibility gaps.
2. Clarify the primary workflow and remove competing emphasis.
3. Normalize typography, spacing, alignment, and control sizing.
4. Convert hard-coded colors to semantic tokens with light and dark variants.
5. Replace vague icons with familiar symbols or clear text labels.
6. Add missing interaction states and accessible names.
7. Simplify nested surfaces, decorative cards, redundant borders, and unnecessary effects.
8. Add material, blur, or motion only after the static hierarchy works.
9. Run the app and inspect the result in real viewports.
10. Iterate until the screen looks intentional, readable, and usable.

## Common Anti-patterns

- Do not copy Apple app layouts, icons, screenshots, marketing pages, or trade dress.
- Do not make Apple-like mean monochrome glass everywhere.
- Do not put cards inside cards or style entire page sections as floating cards.
- Do not use blur behind text when the background can make it illegible.
- Do not use decorative gradient blobs, random glow effects, or one-note palettes as a substitute for hierarchy.
- Do not hide essential actions behind hover-only controls on touch surfaces.
- Do not shrink text or targets just to preserve a desktop layout on mobile.
- Do not animate routine actions so much that people must wait for the UI.
- Do not remove visible focus rings unless replacing them with an equally clear focus style.
- Do not ship a polished screenshot with broken keyboard, screen-reader, dark-mode, or mobile behavior.
## Final Report Expectations
- List changed UI files.
- Mention source references used.
- Summarize layout, color, type, and component changes.
- Call out accessibility and responsive checks.
- State the visual verification method.
- Note skipped checks honestly.
- Avoid claiming Apple compliance unless verified.
- Keep the summary concise.
- Include the local URL when a dev server is running.
- Recommend only concrete next refinements.
- Do not end with a vague optional ask.

## Verification Checklist

- Confirm the primary task is visible without reading explanatory feature text.
- Confirm content, navigation, and controls have clear hierarchy.
- Confirm text remains legible at small widths and larger text settings.
- Confirm contrast meets at least WCAG AA expectations.
- Confirm light and dark modes work, or document why one mode is intentionally absent.
- Confirm every interactive control has label, state, target size, and focus behavior.
- Confirm icon-only controls have accessible names and tooltips where useful.
- Confirm motion is purposeful, brief, interruptible, and reduced under reduced-motion settings.
- Confirm layout works across mobile, tablet, and desktop or the target platform sizes.
- Confirm the result feels native to the target platform while preserving the product's own purpose.
