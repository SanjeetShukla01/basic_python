Data Classes:

Pydantic:

Attrs:





In addition to supplying validator function as argument to the field function we can also use a decorator in attrs
example:

```python
from attrs import Attribute, define, field, validators
@define
class Customer:
    commission: float = field()
    
    @commission.validator
    def _check_percentage(self, attribute, value):
        if not 0 <= value < 1:
            raise ValueError(
                "Commission must be a percentage value between 0 (inclusive) and 1 (exclusive)"
            )
```


- Feature	Dataclass	Attrs	Pydantic
- frozen	✅	✅	✅
- defaults	✅	✅	✅
- totuple	✅	✅	✅
- todict	✅	✅	✅
- validators	❌	✅	✅  This can be implemented usin `__post_init__()` method
- converters	❌	✅	✅
- slotted	❌	✅	❌
- programmatic creation	❌	✅	❌