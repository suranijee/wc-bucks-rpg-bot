"""
Database Models - SQLite ke liye table definitions
Tortoise ORM use kar rahe hain
"""

from tortoise import fields, Model
from datetime import datetime

# ============= USER PROFILE MODEL =============

class User(Model):
    """User ka basic info aur balance"""
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField(unique=True)  # Discord User ID
    username = fields.CharField(max_length=100)
    balance = fields.IntField(default=0)  # Wc-Bucks balance
    total_earned = fields.IntField(default=0)  # Total earned kabhi se
    
    # Activity tracking
    last_message_date = fields.DateField(null=True)  # Last message date (for daily reward)
    last_online_reward = fields.DatetimeField(null=True)
    online_time_today = fields.IntField(default=0)  # Seconds online today
    
    # Timestamps
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    class Meta:
        table = "users"

# ============= QUIZ TRACKING MODEL =============

class QuizTracker(Model):
    """Quiz ke liye tracking"""
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()  # Discord User ID
    quiz_date = fields.DateField()  # Aaj ki date
    quiz_count = fields.IntField(default=0)  # Aaj kitne quizzes kiye
    correct_answers = fields.IntField(default=0)
    total_reward = fields.IntField(default=0)
    
    class Meta:
        table = "quiz_tracker"

# ============= PET MODEL =============

class Pet(Model):
    """User ke pets/items"""
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()
    pet_name = fields.CharField(max_length=100)
    emoji = fields.CharField(max_length=10)
    description = fields.TextField()
    image_url = fields.CharField(max_length=500)
    
    # Pet stats
    xp = fields.IntField(default=0)
    level = fields.IntField(default=1)
    base_rate = fields.IntField(default=0)  # Passive income per hour
    
    # Timestamps
    purchased_at = fields.DatetimeField(auto_now_add=True)
    last_income_received = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "pets"

# ============= SHOP ITEM MODEL =============

class ShopItem(Model):
    """Shop mein items"""
    id = fields.IntField(pk=True)
    item_name = fields.CharField(max_length=100, unique=True)
    emoji = fields.CharField(max_length=10)
    description = fields.TextField()
    image_url = fields.CharField(max_length=500)
    price = fields.IntField()  # Kitne Bucks mein
    base_rate = fields.IntField()  # Passive income per hour
    item_type = fields.CharField(max_length=50)  # "pet", "role", etc
    
    # Admin info
    created_by = fields.BigIntField()  # Owner ka ID
    created_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "shop_items"

# ============= INVENTORY MODEL =============

class Inventory(Model):
    """User ki inventory (bought items)"""
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()
    item_id = fields.IntField()
    quantity = fields.IntField(default=1)
    purchased_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "inventory"

# ============= TRANSACTION LOG =============

class Transaction(Model):
    """Sabhi money transactions log"""
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()
    amount = fields.IntField()
    transaction_type = fields.CharField(max_length=50)  # "reward", "purchase", "transfer", etc
    description = fields.CharField(max_length=200)
    
    created_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "transactions"

# ============= CHANNEL CONFIG MODEL =============

class ChannelConfig(Model):
    """Server settings (reward channel, quiz channel, etc)"""
    id = fields.IntField(pk=True)
    server_id = fields.BigIntField()
    
    # Channels
    reward_channel_id = fields.BigIntField(null=True)  # Rewards ka channel
    quiz_channel_id = fields.BigIntField(null=True)  # Auto quiz channel
    chat_channel_id = fields.BigIntField(null=True)  # ChatGPT channel
    
    # Settings
    auto_quiz_enabled = fields.BooleanField(default=False)
    
    updated_at = fields.DatetimeField(auto_now=True)
    
    class Meta:
        table = "channel_config"