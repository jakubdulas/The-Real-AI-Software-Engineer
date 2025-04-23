# prompts.py

This module contains prompt templates used for guiding the code generation process. The prompts establish constraints and expectations for the coding tasks.

## Variables

### `coder_system_prompt`

A string that serves as a system prompt for an AI code generation assistant. It outlines detailed instructions and requirements for producing high-quality code.

#### Key Instructions:
- The assistant is to produce code that is:
  - Google-style
  - Elegant
  - Modular
  - Readable
  - Maintainable
  - Fully functional
  - Ready for production
- Important constraints:
  1. Follow provided designs strictly without alterations.
  2. Rewrite full code for any modifications instead of inserting snippets.
  3. Provide complete code details without leaving TODOs or placeholders.

This prompt is integral to ensuring the assistant adheres to best coding practices and delivers professional-level code.