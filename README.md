# 纸片化学社区版：数据后端

## 项目介绍

纸片化学社区版（Paper Chemis Community）是由 Tiger 开发的一款纸片化学游戏。该游戏使用纸片化学玩法，并带来了更高的自由度。

本项目为纸片化学社区版的数据后端，为游戏本体提供数据源服务。

## 项目结构

```text
backend/

- run.py
- test/
    - test_*.py
- app/
    - __init__.py
    - models/
    - routes/
        - assets.py
        - cards.py
        - matters.py
        - pages.py
        - reactions.py
    - utils/
        - assets.py
        - cards.py
        - matters.py
        - reactions.py
- resources/
    - assets/
        - index.json
        - pics/
        - sounds/
    - cards/
        - list.json
    - conditions/
        - list.json
    - matters/
        - list.json
    - reactions/
        - list.json
        - match.json
```

## 部分文件格式

### list.json

`cards` `matters` 和 `reactions` `conditions` 下的 `list.json` 有相同的格式。每个文件中都只有一个对象。对象的键的内容均是字符串，代表 ID。对象的值的内容均是字符串，代表对应JSON文件的相对路径，不用加 `.json` 后缀名。例如：

```json
{
    "C": "NonMetal/Carbon",
    "O": "NonMetal/Oxygen",
    "...": "..."
}
```

### reactions/match.json

`reactions` 目录下的 `match.json` 支持通过反应物匹配反应。该文件的内容是一个对象。对象的键由反应物构成，每个反应物（包括最后一个）后面都有一个 `-` 以间隔开各项反应物。值是反应的 ID，即 `list.json` 中对象的键。例如：

```json
{
    "Carbon-Oxygen-": [
        "CarbonDioxide"
    ],
    "...": "..."
}
```

### assets/index.json

`assets` 目录下的 `index.json` 是资源文件的索引目录文件。该文件的内容是一个对象，每一个键值对对应一个资源文件。键对应的是资源的 ID，值对应的是资源的相对文件路径，不加 `pics/` 或 `sounds/` 前缀。例如：

```json
{
    "pics": {
        "Carbon": "cards/Carbon.png",
        "Oxygen": "cards/Oxygen.png",
        "...": "..."
    },
    "sounds": {
        "...": "..."
    }
}
```

## 化学反应格式

化学反应由三部分构成：反应物、反应条件、生成物。反应物写在 `reactants`，反应条件写在 `conditions`，生成物写在 `products`。

其中的反应物 ID、反应物条件 ID、生成物 ID 都是自定义的。也就是说，同一个反应在不同化学源中的表示方式可能不同。

## 技术相关

本项目采用工厂模式。所有逻辑代码均放置在 `app` 目录下。所有路由均使用蓝图实现。

## 最佳实践

不遵守此部分内容引发的问题后果自负。

对于同一物质/卡牌，其在各处的 ID 应该相同，即在 `cards` `matters` `reactions` `assets` 中的 ID 都应该相同，否则游戏本体将无法读取。

对于路径和 ID，均应当使用英文字母、下划线和数字，不应当使用包括中文和短横杠在内的其他字符。

所有 JSON 文件中的缩进均应当使用 2 个或 4 个空格，而非制表符（`\t`）。
