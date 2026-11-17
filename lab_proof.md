# EU AI Act peer audit | Mobile Game Competitor Snapshot

**Reviewer:** Sean Langsdorf · **Builder:** Jędrzej Czarnota · **Status:** Pre-debrief.

- [Two-page audit report](mobile_game_competitor_peer_audit.pdf) and [editable source](mobile_game_competitor_peer_audit.md).
- [Annotated brief, classification and written questions](annotated_brief_and_questions.md). Questions are prepared but not sent. Joint closing note is pending an actual debrief.
- [Builder system brief](evidence/builder_system_brief.md) and [redacted workflow export](evidence/workflow_redacted.json) from [self-audit PR #30](https://github.com/ai-consulting-bootcamp/lab-eu-ai-act-self-audit/pull/30), head `00099b7`. No self-audit conclusions used.
- [Replay code](replay_namespace.js), [test inputs](evidence/namespace_inputs.json) and [captured result](evidence/namespace_output.json).

## Run and result

```sh
node replay_namespace.js evidence/namespace_inputs.json
```

The test inputs are two synthetic studios uploading a playbook and one studio using the default. The offline replay compares the index, namespace and clearing settings used for each route. Both upload routes resolve to the same write and read target with clearing requested. The default route uses `northstar-strategy` and does not write. The workflow export is for evidence only and has been deactivated. Credential bindings, deployment metadata, personal email strings and the original index label were removed or replaced. The namespace logic is unchanged.

**Limitation:** This is a read-only configuration replay. It does not execute n8n, call Pinecone, send email, or establish that any real studios shared an instance, exposed data or lost vectors. The result is conditional on a shared backing index in the hosted deployment.

**Audit outcome:** Limited risk / transparency for the stated intended use. Do not proceed with hosted private uploads or professional launch as configured. See the report for release conditions. Self-audit comparison and joint closing note remain outstanding.
