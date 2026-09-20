import sys
import os
import pytest

def test_python_version():
    assert sys.version_info.major == 3
    assert sys.version_info.minor >=3.10
def test_pytest_availbale():
    assert pytest.__name__ == "pytest"
def test_operation_system():
    current_os = sys.platform
    assert current_os in ["win32","linux","darwin"] , f"Unexpected os:{current_os}"
def test_test_working_directory():
    cwd = os.getcwd()
    assert "p143_CI_Environment_Setup" in cwd
def test_environment_variable():
    env_value = os.getenv("CI ENVIRONMENT","LOCAL")
    assert env_value in ["github-actions", "LOCAL"]
def test_ci_vs_local():
    is_ci = os.getenv("GITHUB_ACTIONS") == True
    if is_ci:
        assert sys.platform== "linux"
    else:
        assert sys.platform == "win32"
    
