import numpy as np
import Pytagoras.calc as Pcl
import pytest
def test_squares():
    '''Test for the example function'''

    # Arrange
    test_variable_1 = 1
    test_variable_2 = 1
    expected_output1 = 1
    expected_output2 = 1

    # Act
    output1, output2 = Pcl.squares(test_variable_1, test_variable_2)

    # Assert
    assert output1 == expected_output1
    assert output2 == expected_output2

    # No cleanup needed
    
    
def test_hypot():
    '''Test for the example function'''

    # Arrange
    opp_sq = 1
    adj_sq = 1
    test_hypot_exp = 1.414 #2135623730951

    # Act
    output1 = Pcl.hypot(opp_sq, adj_sq)

    # Assert
    assert output1 == pytest.approx(test_hypot_exp, abs=1e-3)


    # No cleanup needed
    
def test_slope():
    '''Test for the example function'''

    # Arrange
    opp = 2
    adj = 3
    slope_exp = 3.6056

    # Act
    output1 = Pcl.slope(opp, adj)

    # Assert
    assert np.isclose (output1, slope_exp, atol=1e-3)


    # No cleanup needed