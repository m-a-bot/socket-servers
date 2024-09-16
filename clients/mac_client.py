import unittest

import client1


class MAC(unittest.TestCase):

    def test1(self):

        client = client1.Client(_port=8080)
        client.send("Admin table1 select")
        result = client.receive()
        print(result)
        client.close()

        self.assertNotEqual("Не разрешён доступ!", result)


if __name__ == "__main__":
    unittest.main()