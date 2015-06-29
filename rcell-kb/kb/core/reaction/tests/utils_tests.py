import logging
from django.test import TestCase

import reaction.models as reaction_models
import reaction.utils as reaction_utils

logger = logging.getLogger(__name__)

class CreateReactionNetworkTest(TestCase):
    def test_create_reaction_network(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        logger.error('wazab')
        
        reaction_utils.dot_reaction_graph()
        
        self.fail()