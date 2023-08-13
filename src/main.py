```python
import sys
from src.interfaces.user_interface import UserInterface
from src.interfaces.admin_interface import AdminInterface

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'admin':
        interface = AdminInterface()
    else:
        interface = UserInterface()

    interface.run()

if __name__ == "__main__":
    main()
```