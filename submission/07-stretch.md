# Stretch

## Work Plan: Closing Finding 3 (Photo/OCR Data Retention)

Selected as the strongest remaining open finding, since it's the one most likely to matter once the Sprint 1 multi-distributor rollout begins handling other businesses' customer data, not just one family shop's.

**Deliverable:** A one-page data retention policy note for the photo-intake path, stating: (1) whether images are persisted anywhere after LLM parsing or processed strictly in-memory, (2) if persisted, for how long and why, and (3) a plain-language line for the eventual multi-distributor onboarding flow confirming this behavior to new customers.

**Who would be responsible:** Anand, since this requires direct inspection of the n8n workflow's actual runtime behavior (whether any node writes the incoming image to storage) — not something an external documentation-only audit can determine.

**Realistic timeline:** Same day — this is a five-minute check of the workflow (confirming no image-storage node exists downstream of the vision-parsing step) plus a short paragraph to add to the README. No new engineering work is likely required, only documentation of existing behavior.

**Evidence needed to verify closed:** An explicit line in the README's data-handling section stating the image retention behavior, plus (if any retention exists) a stated retention window. For a stronger long-term verification, a look at the actual n8n execution logs/history settings would confirm whether n8n's own platform-level execution data retention (separate from the workflow's own logic) also stores a copy of the image as part of its execution history — this is a subtlety worth flagging to Anand, since it's a common blind spot: even if the *workflow* doesn't explicitly save the image, the *platform running it* might retain execution data by default.
