# Apple HIG Synthesis for Apple-like UI

This reference distills the official Apple Human Interface Guidelines corpus collected on 2026-04-21 from Apple Developer JSON endpoints. Use it as design guidance, then inspect the source index or refresh the corpus when a task depends on a specific component, platform, or newly changed rule.

Official sources start at:

- https://developer.apple.com/design/human-interface-guidelines
- https://developer.apple.com/design/human-interface-guidelines/foundations
- https://developer.apple.com/design/human-interface-guidelines/layout
- https://developer.apple.com/design/human-interface-guidelines/color
- https://developer.apple.com/design/human-interface-guidelines/materials
- https://developer.apple.com/design/human-interface-guidelines/typography
- https://developer.apple.com/design/human-interface-guidelines/accessibility

## Core Character

Apple-like UI is not just rounded rectangles and blur. It is a disciplined system where content, controls, motion, and language support what people are trying to do. The interface should feel:

- Clear: important content appears first, controls have obvious purpose, copy is brief.
- Deferential: chrome recedes so content and primary tasks lead.
- Adaptive: layout, color, type, input, and motion respond to device, appearance, accessibility, and locale.
- Precise: alignment, spacing, icon weight, typography, states, and transitions look intentionally tuned.
- Familiar: standard platform patterns come before custom interaction inventions.

## Layout and Hierarchy

- Group related items with spacing, alignment, subtle separators, background shapes, or materials.
- Give essential information enough room. Move secondary details into progressive disclosure, secondary panes, sheets, popovers, or contextual menus.
- Extend content to the edges when appropriate, but keep controls inside safe areas and readable margins.
- Align components so scanning feels effortless. Put the most important content near the top and leading side, while respecting right-to-left layout.
- Make controls visually distinct from content. With modern Apple design, controls and navigation often sit in a separate functional layer above content.
- Adapt gracefully to orientation, window resizing, text-size changes, localization, safe areas, display zoom, and external displays.
- Prefer stable responsive changes. Avoid switching to compact layouts until the full layout no longer fits.

## Color and Appearance

- Use semantic colors rather than fixed values. On web, express semantics with CSS variables; in native apps, use system colors.
- Make every custom color work in light, dark, and increased-contrast contexts.
- Use accent color sparingly for primary actions, selection, status, and meaningful emphasis.
- Do not use color as the only indicator of state or meaning. Pair it with text, shape, iconography, or position.
- Test color in different lighting and on different displays. Wide-gamut colors and translucent layers can shift perceived contrast.
- Avoid redefining semantic system colors for unrelated purposes.
- In dark mode, prefer adaptive system backgrounds and labels. For custom colors, maintain sufficient contrast and soften bright white assets.
- For Apple-like web UI, define a restrained neutral palette, one accent family, clear separator/fill colors, and dark-mode equivalents.

## Materials and Depth

- Use material to create hierarchy between foreground controls and background content.
- Use Liquid Glass or glass-like effects sparingly, mainly for navigation, toolbars, tab bars, sidebars, floating controls, sheets, and popovers.
- Do not use glass effects as general content-card decoration. Content layers usually need stable backgrounds or standard materials.
- Choose material by semantic purpose and legibility, not by its apparent color.
- If using clear/translucent glass over rich media, add dimming or stronger blur when needed for contrast.
- Keep text and symbols on materials vibrant and readable. Increase opacity or reduce translucency when contrast suffers.

## Typography

- Use system fonts where possible. On web, use the Apple/system font stack.
- Use built-in text styles or a small type scale that clearly separates title, heading, body, secondary, and caption roles.
- Prefer Regular, Medium, Semibold, and Bold. Avoid ultralight/thin weights, especially below large display sizes.
- Keep typefaces minimal. Too many font families weaken hierarchy and make the interface feel less coherent.
- Support Dynamic Type or browser text zoom. At larger text sizes, stack metadata, reduce columns, and avoid truncating useful content.
- Match icon weight to adjacent text. SF Symbols do this automatically in native Apple UI.

## Controls and Components

- Use standard components whenever possible because they bring familiar behavior, states, accessibility, and appearance adaptation.
- Buttons need enough visible separation and a hit region of at least 44x44 pt or CSS px equivalent; use 60x60 for vision-style spatial targets.
- Custom buttons must have visible pressed, hover, focus, selected, disabled, and loading states as appropriate.
- Use a prominent style for the most likely action, but keep prominent buttons to one or two per view.
- Distinguish a preferred action by style, not by making it a different size from peer actions.
- Never assign primary visual treatment to destructive actions. Use destructive color/role and confirmation where recovery is difficult.
- Use symbols/icons for familiar actions and text labels when words communicate more clearly.
- Menus, sheets, popovers, alerts, tabs, sidebars, toolbars, search fields, segmented controls, toggles, sliders, and lists each have specific HIG pages; consult the source index when implementing them.

## Icons and Symbols

- Icons should express one concept in a simple, recognizable shape.
- Maintain consistent size, visual weight, perspective, detail, stroke, and optical alignment.
- Prefer SF Symbols in native Apple apps. On web, use a simple line icon set already present in the repo and tune stroke weight to text.
- Provide accessible labels for icon-only controls.
- Avoid text inside icons unless essential, and localize or mirror it for right-to-left contexts.
- Do not recreate Apple product hardware or Apple trademarks in custom icons. Do not use SF Symbols in logos or app icons.

## Motion

- Add motion only to communicate feedback, continuity, status, causality, or orientation.
- Keep feedback animations brief, precise, and interruptible.
- Avoid extra animation on interactions people perform frequently.
- Never make motion the only way to understand a state change. Pair it with visual, textual, haptic, or audio feedback.
- Respect reduced-motion settings. Replace large movements, zooms, depth changes, repeated bounces, peripheral motion, and blur animations with simpler fades or instant state changes.
- For spatial/vision-style UI, avoid peripheral motion, large moving objects, world rotation, sustained oscillation, and head-locked content.

## Accessibility and Inclusion

- Audit for perceivable, intuitive, and adaptable interaction.
- Meet contrast expectations; WCAG AA guidance is at least 4.5:1 for normal text and 3:1 for larger or bold text.
- Support larger text, keyboard navigation, screen readers, voice control, pointer/touch, and assistive technologies.
- Controls should be large enough and spaced enough to avoid accidental activation.
- Offer alternatives to gestures, audio-only cues, color-only cues, and timed auto-dismissal.
- Label icons, images, form fields, buttons, and custom controls for assistive technologies.
- Use inclusive imagery and language. Avoid gendered, culturally narrow, or jargon-heavy symbols and copy.

## Writing

- Use plain language. Keep only words that help people act or understand.
- Label actions with verbs: "Send", "Add to Cart", "Continue", "Done".
- Match tone to context. Serious moments need direct language; celebratory moments can be warmer.
- Keep terminology consistent across flows.
- Empty states should explain the next useful action and include a path to take it.
- Error messages should be near the problem, blame-free, and specific about how to recover.
- For settings, label the on-state clearly and let people infer the off-state.
- Use device-appropriate verbs: "tap" for touch, "click" for pointer, "press" when platform conventions call for it.

## Platform Cues

- iOS: prioritize the primary task, limit onscreen controls, support orientation and Dynamic Type, put common controls where thumbs can reach, and use swipes/navigation patterns people expect.
- iPadOS: design for resizing and multitasking; prefer adaptable navigation such as sidebars or adaptable tab bars when the app complexity warrants it.
- macOS: respect window behavior, menu bar conventions, keyboard shortcuts, toolbars, sidebars, and pointer/hover affordances.
- watchOS: keep views focused, glanceable, edge-to-edge, and sparing with side-by-side controls.
- tvOS: design for focus, distance viewing, large text, remote input, safe areas, and subtle scale/focus animations.
- visionOS: prioritize comfort, depth restraint, spatial legibility, large gaze-friendly controls, stable windows, and materials that keep people grounded.
- Web: translate the principles without pretending to be a native Apple app. Use semantic HTML, responsive CSS, system font stacks, accessible states, and restrained material effects.

## Practical Design Pass

When improving an existing UI:

1. Remove visual noise before adding polish.
2. Clarify the primary action and reduce competing emphasis.
3. Normalize spacing, alignment, and type scale.
4. Convert hard-coded colors to semantic tokens with light/dark variants.
5. Replace vague icons with familiar symbols or clear text.
6. Add missing states: hover, active, focus-visible, disabled, selected, loading, empty, error.
7. Check hit targets and keyboard/screen-reader behavior.
8. Add subtle, reduced-motion-safe transitions only after the static UI works.
