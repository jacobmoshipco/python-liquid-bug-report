# python-liquid bug report 228

Run `uv run liquid-bug-report` for demonstration

---

Since 2.3.3, `>=` and `<=` evaluate to `false` when both operands are equal. This applies to integers, floats and strings.

```python
from liquid import parse

for expr in ["1 >= 1", "1 <= 1", "1.5 >= 1.5", '"a" >= "a"', "2 >= 1"]:
    print(expr, parse("{% if " + expr + " %}true{% else %}false{% endif %}").render())
```

| Expression   | 2.3.2  | 2.3.3   |
|--------------|--------|---------|
| `1 >= 1`     | `true` | `false` |
| `1 <= 1`     | `true` | `false` |
| `1.5 >= 1.5` | `true` | `false` |
| `"a" >= "a"` | `true` | `false` |
| `"a" <= "a"` | `true` | `false` |
| `2 >= 1`     | `true` | `true`  |

It looks like it came in on [#222](https://github.com/jg-rp/liquid/pull/222). `LeExpression` and `GeExpression` now call the new `_le` helper in `liquid/builtin/expressions/logical.py`. Its string and number branches return `left < right` instead of `left <= right`, so the equality case is lost.
