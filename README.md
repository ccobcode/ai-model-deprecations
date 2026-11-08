# AI model deprecation calendar

Shutdown, reroute and price-change dates for models on the OpenAI, Anthropic and Google Gemini APIs, copied from each provider's official deprecation, release-note and pricing pages. Every entry links to its source.

Use it as data or subscribe to it as a calendar:

- **JSON:** [`data/changes.json`](data/changes.json), raw at `https://raw.githubusercontent.com/ccobcode/ai-model-deprecations/main/data/changes.json`
- **Calendar (iCal):** `https://raw.githubusercontent.com/ccobcode/ai-model-deprecations/main/calendar.ics`. In Google Calendar choose Other calendars, From URL. In Apple Calendar choose File, New Calendar Subscription. In Outlook choose Add calendar, Subscribe from web.

Each calendar event covers one provider on one day and lists every model that changes, its replacement and the source page.

## Upcoming changes

<!-- table:start -->
Checked against the official pages on 2026-11-08. 54 entries.

| Date | Provider | Change | Model | Replacement | Source |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 2026-11-17 | Google | shutdown | `gemini-2.5-flash-native-audio-preview-12-2025` | `gemini-3.8-live`. Google lists the earliest possible shutdown date. | [link](https://aistudio.google.com/docs/deprecations) |
| 2026-11-17 | Google | shutdown | `gemini-2.5-flash-preview-tts` | gemini-3.8-flash-tts or gemini-3.8-flash-lite-tts. Google lists the earliest possible shutdown date. | [link](https://aistudio.google.com/docs/deprecations) |
| 2026-11-17 | Google | shutdown | `gemini-2.5-pro-preview-tts` | gemini-3.8-flash-tts or gemini-3.8-flash-lite-tts. Google lists the earliest possible shutdown date. | [link](https://aistudio.google.com/docs/deprecations) |
| 2026-11-17 | Google | shutdown | `gemini-3.1-flash-live-preview` | `gemini-3.8-live`. Google lists the earliest possible shutdown date. | [link](https://aistudio.google.com/docs/deprecations) |
| 2026-11-17 | Google | shutdown | `gemini-3.1-flash-tts-preview` | gemini-3.8-flash-tts or gemini-3.8-flash-lite-tts. Google lists the earliest possible shutdown date. | [link](https://aistudio.google.com/docs/deprecations) |
| 2026-11-30 | Anthropic | feature | `claude-opus-4-8` | `claude-opus-5-5`. Fast mode removed: requests with speed "fast" return an error. | [link](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-11-30 | Anthropic | shutdown | `claude-sonnet-4-5-20250929` | `claude-sonnet-5-5`. Retirement on the Claude API. | [link](https://platform.claude.com/docs/en/about-claude/model-deprecations) |
| 2026-11-30 | OpenAI | shutdown | Agent Builder | Agents SDK or ChatGPT Workspace Agents | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-11-30 | OpenAI | shutdown | Evals dashboard and API | `Promptfoo` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-11-30 | OpenAI | price | `gpt-5.6-sol` | Promotional pricing ($4 input / $20 output per 1M tokens) ends; the later price is not published on the model page. | [link](https://developers.openai.com/api/docs/models/gpt-5.6-sol) |
| 2026-11-30 | OpenAI | shutdown | `v1/prompts` | Prompt content in your own code. The v1/prompts API and reusable prompt objects shut down. | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-12-01 | Google | reroute | `gemini-2.5-flash` | `gemini-3.5-flash-lite`. Requests keep working but are answered by and billed as gemini-3.5-flash-lite. | [link](https://aistudio.google.com/docs/deprecations) |
| 2026-12-01 | Google | reroute | `gemini-2.5-pro` | `gemini-3.8-flash`. Requests keep working but are answered by and billed as gemini-3.8-flash. | [link](https://aistudio.google.com/docs/deprecations) |
| 2026-12-01 | Google | price | `gemini-4-argon` | $2 / $10 per 1M input / output tokens becomes $4 / $20; cached input $0.10 becomes $0.20. | [link](https://aistudio.google.com/docs/pricing) |
| 2026-12-01 | OpenAI | shutdown | `chatgpt-image-latest` | gpt-image-2.6-sunburst or gpt-image-2.6-flare | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-12-01 | OpenAI | shutdown | `gpt-image-1-mini` | gpt-image-2.6-sunburst or gpt-image-2.6-flare | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-12-01 | OpenAI | shutdown | `gpt-image-1.5`<br>`gpt-image-1.5-2025-12-16` | gpt-image-2.6-sunburst or gpt-image-2.6-flare | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-12-11 | OpenAI | shutdown | `gpt-5`<br>`gpt-5-2025-08-07` | `gpt-5.6-sol`. Fine-tuned versions follow the base model. | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-12-11 | OpenAI | shutdown | `gpt-5-mini`<br>`gpt-5-mini-2025-08-07` | `gpt-5.6-terra`. Fine-tuned versions follow the base model. | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-12-11 | OpenAI | shutdown | `gpt-5-nano`<br>`gpt-5-nano-2025-08-07` | `gpt-5.6-luna`. Fine-tuned versions follow the base model. | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-12-11 | OpenAI | shutdown | `gpt-5-pro`<br>`gpt-5-pro-2025-10-06` | gpt-5.6-sol (reasoning.mode: pro). Fine-tuned versions follow the base model. | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-12-11 | OpenAI | shutdown | `o3`<br>`o3-2025-04-16` | `gpt-5.6-sol`. Fine-tuned versions follow the base model. | [link](https://developers.openai.com/api/docs/deprecations) |
| 2026-12-11 | OpenAI | shutdown | `o3-pro`<br>`o3-pro-2025-06-10` | gpt-5.6-sol (reasoning.mode: pro). Fine-tuned versions follow the base model. | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-01 | Google | price | `gemini-3.6-flash` | $0.75 / $3.75 per 1M input / output tokens becomes $1.50 / $7.50; cached input $0.075 becomes $0.15. | [link](https://aistudio.google.com/docs/pricing) |
| 2027-01-01 | Google | price | `gemini-3.8-flash` | $0.75 / $3.75 per 1M input / output tokens becomes $1.50 / $7.50; cached input $0.075 becomes $0.15. | [link](https://aistudio.google.com/docs/pricing) |
| 2027-01-06 | OpenAI | feature | Fine-tuning jobs | Active existing customers can no longer create new fine-tuning jobs. Inference on fine-tuned models continues until the base model is deprecated. | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-06 | OpenAI | shutdown | `gpt-4o-mini-tts`<br>`gpt-4o-mini-tts-2025-03-20`<br>`gpt-4o-mini-tts-2025-12-15` | `gpt-realtime-2.1-mini` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-06 | OpenAI | shutdown | `tts-1` | `gpt-realtime-2.1-mini` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-06 | OpenAI | shutdown | `tts-1-hd` | `gpt-realtime-2.1-mini` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-14 | OpenAI | shutdown | `gpt-4.1-2025-04-14` | `gpt-6-luna` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-14 | OpenAI | shutdown | `gpt-4.1-mini-2025-04-14` | `gpt-6-luna` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-14 | OpenAI | shutdown | `gpt-4o-2024-08-06` | `gpt-6-luna` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-14 | OpenAI | shutdown | `gpt-4o-2024-11-20` | `gpt-6-luna` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-14 | OpenAI | shutdown | `gpt-4o-mini-2024-07-18` | `gpt-6-luna` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-20 | OpenAI | shutdown | `gpt-4o-audio` | `gpt-audio-1.5` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-20 | OpenAI | shutdown | `gpt-4o-mini-audio` | `gpt-audio-1.5` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-20 | OpenAI | shutdown | `gpt-4o-mini-realtime` | `gpt-realtime-2.1-mini` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-20 | OpenAI | shutdown | `gpt-4o-mini-transcribe-2025-03-20` | `gpt-4o-mini-transcribe-2025-12-15` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-20 | OpenAI | shutdown | `gpt-4o-realtime` | `gpt-realtime-2.1` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-20 | OpenAI | shutdown | `gpt-audio`<br>`gpt-audio-2025-08-28` | `gpt-audio-1.5` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-20 | OpenAI | shutdown | `gpt-audio-mini`<br>`gpt-audio-mini-2025-12-15` | `gpt-audio-1.5` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-20 | OpenAI | shutdown | `gpt-realtime`<br>`gpt-realtime-2025-08-28` | `gpt-realtime-2.1` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-01-20 | OpenAI | shutdown | `gpt-realtime-mini`<br>`gpt-realtime-mini-2025-12-15` | `gpt-realtime-2.1-mini` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-02-01 | OpenAI | shutdown | `gpt-5.5-cyber-preview` | The most capable cyber model available to you | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-02-26 | OpenAI | shutdown | `/v1/audio/translations` | `v1/realtime/translations` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-02-26 | OpenAI | shutdown | `gpt-4o-mini-transcribe`<br>`gpt-4o-mini-transcribe-2025-12-15` | gpt-live-transcribe or gpt-transcribe | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-02-26 | OpenAI | shutdown | `gpt-4o-transcribe` | gpt-live-transcribe or gpt-transcribe | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-02-26 | OpenAI | shutdown | `gpt-4o-transcribe-diarize` | gpt-live-transcribe or gpt-transcribe | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-02-26 | OpenAI | shutdown | `whisper-1` | gpt-live-transcribe or gpt-transcribe | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-03-15 | Google | shutdown | `gemini-2.5-flash-image` | `gemini-3.1-flash-lite-image`. Google lists the earliest possible shutdown date. | [link](https://aistudio.google.com/docs/deprecations) |
| 2027-04-01 | OpenAI | shutdown | `gpt-5.1`<br>`gpt-5.1-2025-11-13` | `gpt-6-sol` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-04-01 | OpenAI | shutdown | `gpt-5.3-codex` | `gpt-6-sol` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-04-01 | OpenAI | shutdown | `gpt-5.4-nano`<br>`gpt-5.4-nano-2026-03-17` | `gpt-6-luna` | [link](https://developers.openai.com/api/docs/deprecations) |
| 2027-05-07 | Google | shutdown | `gemini-3.1-flash-lite` | `gemini-3.5-flash-lite`. Google lists the earliest possible shutdown date. | [link](https://aistudio.google.com/docs/deprecations) |
<!-- table:end -->

## How to read the dates

- **shutdown:** requests to the model ID fail after this date. Google lists the earliest possible shutdown date, so a Gemini model can stay up a little longer.
- **reroute:** the model ID keeps answering, but a newer model replies and you are billed at that model's rates. No error tells you the model changed.
- **price:** the per-token price of a model that stays available changes on this date.
- **feature:** the model stays, but a feature or endpoint behavior changes.

Dates cover each provider's own API (OpenAI API, Claude API, Gemini Developer API). Amazon Bedrock, Microsoft Foundry and Vertex AI run their own schedules.

## Migration guides

- [GPT-5 and o3 shut down on December 11, 2026: replacements, prices and code changes](https://www.vtoken.cc/blog/tutorials/gpt-5-o3-shutdown-migration-guide)
- [Claude Sonnet 4.5 retires on November 30, 2026: how to migrate to Claude Sonnet 5.5](https://www.vtoken.cc/blog/tutorials/claude-sonnet-4-5-retirement-migration-guide)
- [Gemini 2.5 Pro and 2.5 Flash reroute on December 1, 2026](https://www.vtoken.cc/blog/tutorials/gemini-2-5-pro-flash-reroute-migration-guide)

## Sources

- OpenAI [deprecations](https://developers.openai.com/api/docs/deprecations) and [GPT-5.6 Sol model page](https://developers.openai.com/api/docs/models/gpt-5.6-sol)
- Anthropic [model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) and [release notes](https://platform.claude.com/docs/en/release-notes/overview)
- Google [Gemini API deprecations](https://aistudio.google.com/docs/deprecations) and [pricing](https://aistudio.google.com/docs/pricing)

## Contributing

Open an issue or a pull request with a link to the official page that announces the change. Edit `data/changes.json`, then run `python3 scripts/build.py` to regenerate `calendar.ics` and the table above. Entries without an official source are not added.

## License

The data and text are available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Link back to this repository when you reuse them.

Maintained by [vToken](https://www.vtoken.cc), an AI API gateway that publishes [AI API news and migration guides](https://www.vtoken.cc/blog).
