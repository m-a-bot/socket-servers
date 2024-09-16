import unittest
import client1

class RBAC(unittest.TestCase):

    def test1(self):

        client = client1.Client()
        client.send("Admin table1 select")
        result = client.receive()
        print(result)
        client.close()

        self.assertNotEqual("Не разрешён доступ!", result)


if __name__ == "__main__":
    unittest.main()