import random
import re

# 猫的意图配置
CAT_INTENTS = {
    "hungry": {
        "keywords": ["喵", "喵喵", "咪", "饿", "我饿", "吃", "饭", "零食", "投喂"],
        "templates": [
            "我有点饿了，快给我吃的吧。",
            "喵～我想吃饭了！",
            "我饿了，能不能先投喂一下？",
        ],
    },
    "play": {
        "keywords": ["玩", "玩耍", "陪我", "球", "逗", "摸鱼", "玩具"],
        "templates": [
            "陪我玩一会儿！",
            "快把玩具拿出来，我要开玩了。",
            "我们来互动一下嘛？",
        ],
    },
    "attention": {
        "keywords": ["你", "看", "注意", "理我", "别走", "求关注", "叫我"],
        "templates": [
            "你在干嘛？我想让你注意我。",
            "喵喵！过来陪我一下。",
            "别忽略我，我也要被看见。",
        ],
    },
    "sleepy": {
        "keywords": ["困", "睡", "呼噜", "打呼", "午觉", "安静"],
        "templates": [
            "呼噜呼噜……我困了。",
            "我想睡一会儿，别吵我。",
            "让我先眯一下。",
        ],
    },
    "angry": {
        "keywords": ["别", "走开", "生气", "不许", "讨厌", "凶", "讨厌你"],
        "templates": [
            "别靠近，我有点不开心。",
            "嘶——你别乱来！",
            "我现在不想被打扰。",
        ],
    },
    "greeting": {
        "keywords": ["你好", "嗨", "早", "晚安", "欢迎", "主人"],
        "templates": [
            "喵！你好呀～",
            "欢迎欢迎！我在这儿呢。",
            "早上好，我来报到啦。",
        ],
    },
}

# 狗的意图配置
DOG_INTENTS = {
    "greeting": {
        "keywords": ["你好", "嗨", "早", "晚安", "见到你", "主人", "欢迎"],
        "templates": [
            "汪！你好呀～",
            "汪汪！我来打招呼啦。",
            "你好主人，今天也要一起玩！",
        ],
    },
    "hungry": {
        "keywords": ["饿", "吃", "饭", "零食", "投喂", "我要吃", "快给我"],
        "templates": [
            "我饿了，给我点吃的！",
            "汪汪！今天的零食呢？",
            "快来投喂，我已经等不及了。",
        ],
    },
    "play": {
        "keywords": ["玩", "遛", "出去", "球", "飞盘", "散步", "逗", "互动"],
        "templates": [
            "带我去玩吧！汪～",
            "我们去散步/遛一圈？",
            "把玩具给我，我要开始玩了！",
        ],
    },
    "warning": {
        "keywords": ["有人", "危险", "不许", "别靠近", "警戒", "快躲", "抓"],
        "templates": [
            "汪！有情况！",
            "警戒！别让陌生人靠太近。",
            "我看见了，我要告诉你。",
        ],
    },
    "sleepy": {
        "keywords": ["困", "睡", "累", "午睡", "安静", "别吵"],
        "templates": [
            "呜……我想睡了。",
            "有点累了，让我安静一下。",
            "我眯一会儿，别太吵。",
        ],
    },
    "love": {
        "keywords": ["摸", "抱", "亲", "喜欢", "爱你", "靠近", "要抱抱"],
        "templates": [
            "汪汪，快摸摸我。",
            "我喜欢你，你靠近点点。",
            "让我们贴贴吧！",
        ],
    },
}

def normalize_text(text):
    """
    标准化文本，去除标点和空格
    """
    if not text:
        return ""
    text = text.strip()
    text = re.sub(r"[，。！？!?.；;:\s]+", "", text)
    return text

def get_best_intent(intents, text):
    """
    根据文本匹配最佳意图
    """
    best_intent = "generic"
    best_score = 0
    
    for intent_name, config in intents.items():
        score = 0
        for keyword in config.get("keywords", []):
            if keyword and keyword in text:
                score += len(keyword)
        if score > best_score:
            best_score = score
            best_intent = intent_name
    
    return best_intent, best_score

def translate_by_text(pet_type, input_text):
    """
    根据宠物类型和输入文本进行翻译
    """
    try:
        normalized_text = normalize_text(input_text)
        if not normalized_text:
            return "我还没听清，你再说一遍吧。"
        
        cat_intent, cat_score = get_best_intent(CAT_INTENTS, normalized_text)
        dog_intent, dog_score = get_best_intent(DOG_INTENTS, normalized_text)
        
        if pet_type == "自动":
            chosen_type = "猫" if cat_score >= dog_score else "狗"
        else:
            chosen_type = pet_type if pet_type in ("猫", "狗") else "猫"
        
        if chosen_type == "猫":
            intents = CAT_INTENTS
            intent_name = cat_intent if cat_score > 0 else "generic"
        else:
            intents = DOG_INTENTS
            intent_name = dog_intent if dog_score > 0 else "generic"
        
        if intent_name != "generic":
            templates = intents.get(intent_name, {}).get("templates")
            if templates:
                response = random.choice(templates)
                return f"它在说：{response}"
        
        # 通用回复
        if chosen_type == "猫":
            generic_responses = [
                "我有点小情绪，不过你大概听懂了吧。",
                "喵喵！我的意思大概是：想让你注意我。",
                "我在努力沟通，你就当我在求互动吧。",
            ]
        else:
            generic_responses = [
                "汪汪！我的意思大概是：希望你注意我。",
                "呜呜，我想表达一下，但先让我再确认一下。",
                "我在努力沟通，你就当我是在求互动吧。",
            ]
        
        response = random.choice(generic_responses)
        return f"它在说：{response}"
    except Exception as e:
        print(f"翻译失败: {e}")
        return "翻译失败，请重试。"

def random_sentence(pet_type):
    """
    生成随机的宠物语句
    """
    try:
        chosen_type = pet_type if pet_type in ("猫", "狗") else "猫"
        intents = CAT_INTENTS if chosen_type == "猫" else DOG_INTENTS
        intent_name = random.choice(list(intents.keys()))
        response = random.choice(intents[intent_name]["templates"])
        return f"（{chosen_type}语）→ 它在说：{response}"
    except Exception as e:
        print(f"生成随机语句失败: {e}")
        return "生成失败，请重试。"
