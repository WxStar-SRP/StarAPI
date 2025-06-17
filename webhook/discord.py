import aiohttp
from dotenv import dotenv_values
from database.db_models import WXStar
from datetime import datetime, tzinfo

env = dotenv_values('.env')

async def log_unit_creation(unit_info: WXStar):
    embed = {
        "embeds": [
            {
                "title": "New Unit Registered",
                "description": str(unit_info.id),
                "color": 2326507,
                "fields": [
                    {
                        "name": "Name",
                        "value": unit_info.name,
                        "inline": True
                    },
                    {
                        "name": "MSO Code",
                        "value": str(unit_info.msocode),
                        "inline": True
                    },
                    {
                        "name": "Unit Model",
                        "value": unit_info.model,
                        "inline": True
                    },
                    {
                        "name": "Flavor (LF)",
                        "value": unit_info.gfxpkg_lf,
                        "inline": True
                    },
                    {
                        "name": "Flavor (LDL)",
                        "value": unit_info.gfxpkg_ldl,
                        "inline": True
                    }
                ],
                "author": {
                    "name": "StarAPI",
                    "url": "https://github.com/wxstar-utils/starapi",
                    "icon_url": "https://avatars.githubusercontent.com/u/213566122?s=200&v=4"
                }
            }
        ],
        "username": "StarAPI Logging",
        "avatar_url": "https://avatars.githubusercontent.com/u/213566122?s=200&v=4"
    }

    async with aiohttp.ClientSession() as session:
        try:
            await session.post(env['DISCORD_WEBHOOK_URL'], json=embed)
        except:
            pass
