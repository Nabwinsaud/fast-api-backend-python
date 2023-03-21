import asyncio
from prisma import Prisma
from prisma.models import User


#  typescript java
async def main() -> None:
    db = Prisma(auto_register=True)
    await db.connect()

    user = await User.prisma().create(data={'name': "Nabin saud", "email": "nabin@gmail.com"})
    print('user created successfully')
    read_user = await User.prisma().find_many()
    print('user data is', read_user)
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
