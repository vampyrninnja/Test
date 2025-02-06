from pytest import mark

@mark.body
class BodyTests:
    @mark.door
    @mark.smoke
    def test_body(self):
        assert True

    def test_bumper(self):
        assert True
    @mark.three
    def test_windshield(self):
        assert True