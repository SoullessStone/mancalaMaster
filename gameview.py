
        self.assertFalse(result)

    def test_isLegalMove_Player2_0(self):
        sut = Game();
        sut.gameModel.switchTurn();
        print(sut.isMinTurn());
        print("bla");

        result = sut.isLegalMove(0);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_1(self):
        sut = Game();

        result = sut.isLegalMove(1);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_2(self):
        sut = Game();

        result = sut.isLegalMove(2);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_3(self):
        sut = Game();

        result = sut.isLegalMove(3);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_4(self):
        sut = Game();

        result = sut.isLegalMove(4);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_5(self):
        sut = Game();

        result = sut.isLegalMove(5);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_6(self):
        sut = Game();

        result = sut.isLegalMove(6);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_7(self):
        sut = Game();

        result = sut.isLegalMove(67);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_8(self):
        sut = Game();

        result = sut.isLegalMove(8);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_8(self):
        sut = Game();

        result = sut.isLegalMove(9);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_10(self):
        sut = Game();

        result = sut.isLegalMove(10);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_11(self):
        sut = Game();

        result = sut.isLegalMove(11);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_12(self):
        sut = Game();

        result = sut.isLegalMove(12);        

        print("isLegalMove: " + str(result))
        self.assertTrue(result)

    def test_isLegalMove_Player2_13(self):
        sut = Game();

        result = sut.isLegalMove(13);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)

    def test_isLegalMove_Player2_14(self):
        sut = Game();

        result = sut.isLegalMove(14);        

        print("isLegalMove: " + str(result))
        self.assertFalse(result)
