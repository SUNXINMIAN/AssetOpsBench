from mcphub import ToolUniverse

tu = ToolUniverse()
tu.load_tools()

result = tu.run({
    "name": "iot.installed_sensors",
    "arguments": {
        "site_name": "MAIN",
        "asset_id": "Chiller 6",
    },
})

print(result)
tu.close()