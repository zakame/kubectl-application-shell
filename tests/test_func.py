"""Testing .func"""

import pytest

from kubectl_application_shell import func


def test_get_api_client():
    """Test get_api_client."""
    assert func.get_api_client()
    assert isinstance(func.get_api_client(), func.client.ApiClient)


def test_get_api_client_incluster_config():
    """Test get_api_client with incluster config."""
    with pytest.raises(func.config.config_exception.ConfigException):
        func.get_api_client("no-such-context")


def test_get_kube_version():
    """Test get_kube_version."""
    assert func.get_kube_version()
    assert isinstance(func.get_kube_version(), str)


def test_get_kubectl():
    """Test get_kubectl."""
    version = "v1.31.5"
    assert func.get_kubectl(version)
    assert isinstance(func.get_kubectl(version), func.Path)


def test_get_deployment_info():
    """Test get_deployment_info."""
    assert func.get_deployment_info("kube-system", "coredns")
    assert isinstance(func.get_deployment_info("kube-system", "coredns"), dict)
