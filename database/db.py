"""
Database Connection Setup
"""

from tortoise import Tortoise
import logging

logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite://db.sqlite3"

async def init_db():
    """Database initialize karo"""
    try:
        await Tortoise.init(
            db_url=DATABASE_URL,
            modules={'models': ['database.models']}
        )
        await Tortoise.generate_schemas()
        logger.info("✅ Database initialized successfully!")
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        raise

async def close_db():
    """Database connection close karo"""
    await Tortoise.close_connections()
    logger.info("✅ Database connection closed!")
