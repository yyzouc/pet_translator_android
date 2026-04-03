import random
import re


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


def _normalize_text(s: str) -> str:
    s = (s or "").strip()
    # 去掉常见标点、空格，方便包含匹配
    s = re.sub(r"[，。！？!?.；;:\s]+", "", s)
    return s


def _best_intent(intents: dict, text_norm: str) -> tuple[str, int]:
    best_key = "generic"
    best_score = 0

    for intent_key, cfg in intents.items():
        score = 0
        for kw in cfg.get("keywords", []):
            if kw and kw in text_norm:
                score += len(kw)
        if score > best_score:
            best_score = score
            best_key = intent_key

    return best_key, best_score


def translate_by_text(pet_type: str, raw_input: str) -> str:
    """
    pet_type: "猫" | "狗" | "自动"
    raw_input: 语音识别后的中文文本
    """
    text_norm = _normalize_text(raw_input)
    if not text_norm:
        return "我还没听清，你再说一遍吧。"

    cat_intents = CAT_INTENTS
    dog_intents = DOG_INTENTS

    cat_intent, cat_score = _best_intent(cat_intents, text_norm)
    dog_intent, dog_score = _best_intent(dog_intents, text_norm)

    if pet_type == "自动":
        chosen = "猫" if cat_score >= dog_score else "狗"
    else:
        chosen = pet_type if pet_type in ("猫", "狗") else "猫"

    intents = cat_intents if chosen == "猫" else dog_intents
    if chosen == "猫":
        intent_key = cat_intent if cat_score > 0 else "generic"
        templates = intents.get(intent_key, {}).get("templates") if intent_key != "generic" else None
    else:
        intent_key = dog_intent if dog_score > 0 else "generic"
        templates = intents.get(intent_key, {}).get("templates") if intent_key != "generic" else None

    if templates:
        response = random.choice(templates)
        return f"它在说：{response}"

    # generic兜底
    if chosen == "猫":
        generic = [
            "我有点小情绪，不过你大概听懂了吧。",
            "喵喵！我的意思大概是：想让你注意我。",
            "我在努力沟通，你就当我在求互动吧。",
        ]
        return f"它在说：{random.choice(generic)}"

    generic = [
        "汪汪！我的意思大概是：希望你注意我。",
        "呜呜，我想表达一下，但先让我再确认一下。",
        "我在努力沟通，你就当我是在求互动吧。",
    ]
    return f"它在说：{random.choice(generic)}"


def random_sentence(pet_type: str) -> str:
    pet_type = pet_type if pet_type in ("猫", "狗") else "猫"
    intents = CAT_INTENTS if pet_type == "猫" else DOG_INTENTS
    intent_key = random.choice(list(intents.keys()))
    response = random.choice(intents[intent_key]["templates"])
    return f"（{pet_type}语）→ 它在说：{response}"

