# Alumnium MCP Server

Model Context Protocol (MCP) server for Alumnium - enables AI coding agents like Claude Code to use Alumnium for automated test generation.

## Quick Start

### Installation

```bash
pip install alumnium
```

### Configuration for Claude Code

Add to your Claude Code MCP settings (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "alumnium": {
      "command": "alumnium-mcp",
      "env": {
        "ALUMNIUM_MODEL": "anthropic/claude-haiku-4-5-20251001",
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}"
      }
    }
  }
}
```

**Note:** The MCP server defaults to Claude Haiku for optimal performance and cost. Alumnium works better with Haiku than frontier models.

### Usage

Once configured, you can ask Claude Code to:

```
"Start a Chrome browser and test the login flow on example.com"
```

Claude Code will use Alumnium MCP tools to:
1. Start a browser
2. Navigate and interact with the page
3. Verify functionality
4. Generate the test code for you

## Available Tools

- `alumnium_start_driver` - Initialize browser/mobile driver
- `alumnium_do` - Execute actions via natural language
- `alumnium_check` - Verify statements about the page
- `alumnium_get` - Extract data from the page
- `alumnium_area` - Create scoped area for focused operations
- `area_do`, `area_check`, `area_get` - Area-scoped operations
- `alumnium_get_accessibility_tree` - Debug page structure
- `alumnium_quit_driver` - Cleanup driver

## Example Workflow

```python
# What the AI agent does behind the scenes:

# 1. Start browser
driver_id = alumnium_start_driver(platform="chromium", url="https://example.com")

# 2. Interact
alumnium_do(driver_id, "click login button")
alumnium_do(driver_id, "type 'user@example.com' in email field")
alumnium_do(driver_id, "type 'password123' in password field")
alumnium_do(driver_id, "click submit button")

# 3. Verify
alumnium_check(driver_id, "page title contains 'Dashboard'")
username = alumnium_get(driver_id, "displayed username")

# 4. Generate test code based on the successful interaction
# AI creates the final test file with Alumni API calls

# 5. Cleanup
alumnium_quit_driver(driver_id)
```

## Testing the MCP Server

Use the MCP Inspector to test:

```bash
npx @modelcontextprotocol/inspector alumnium-mcp
```

## Model Configuration

By default, the MCP server uses Claude Haiku (`claude-haiku-4-5-20251001`) for better performance with Alumnium.

You can override this with the `ALUMNIUM_MODEL` environment variable:

```bash
ALUMNIUM_MODEL="openai/gpt-4o-mini" alumnium-mcp
```

Supported models:
- `anthropic/claude-haiku-4-5-20251001` (recommended)
- `openai/gpt-4o-mini`
- `google/gemini-2.0-flash-001`
- And others supported by Alumnium

## Requirements

- Python 3.10+
- Chrome/Chromium (for `platform="chromium"`)
- Appropriate API keys (ANTHROPIC_API_KEY, OPENAI_API_KEY, etc.)

## Troubleshooting

**Driver not starting:**
- Ensure Chrome/Chromium is installed
- Check that chromedriver is in PATH

**Model errors:**
- Verify API keys are set correctly
- Check `ALUMNIUM_MODEL` environment variable

**MCP connection issues:**
- Restart Claude Code after configuration changes
- Check MCP server logs in Claude Code settings
