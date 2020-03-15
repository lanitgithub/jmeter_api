import xmltodict
import pytest

from jmeter_api.basics.jsr223 import JSR223, ScriptLanguage


class TestJSR223:
    class TestCacheKey:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223(cache_key="True")

        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223(cache_key="1")

        def test_positive(self):
            JSR223(cache_key=True)

    class TestFilename:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223(filename=1)

        def test_check2(self):
            with pytest.raises(OSError):
                JSR223(filename="notExestingFile")

        def test_positive(self):
            JSR223(filename="./jmeter_api/basics/jsr223_test.groovy")

    class TestScript:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223(script=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223(script=False)

        def test_positive(self):
            JSR223(script="var a=0")
            
    class TestParameters:
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223(parameters=1)
                
        def test_check2(self):
            with pytest.raises(TypeError):
                JSR223(parameters=False)

        def test_positive(self):
            JSR223(parameters="some parameters")

    class TestScriptLanguage:                
        def test_check(self):
            with pytest.raises(TypeError):
                JSR223(script_language='java')

        def test_positive(self):
            JSR223(script_language=ScriptLanguage.JAVA)
