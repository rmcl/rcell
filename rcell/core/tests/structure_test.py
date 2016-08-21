import unittest
import mock

import rcell.core as core
import rcell.core.exceptions as core_exceptions


class TestStructureContainerMixin(unittest.TestCase):

    class StructureContainerMixinMock(core.StructureContainerMixin):
        pass

    def test_can_add_and_retrieve_structures(self):
        structure_mock = mock.Mock
        container = TestStructureContainerMixin.StructureContainerMixinMock()
        container.add_structure('awesome', structure_mock)

        self.assertEquals(['awesome'], container.structures.keys())

    def test_cannot_add_same_structure_name_twice(self):
        structure_mock = mock.Mock
        container = TestStructureContainerMixin.StructureContainerMixinMock()
        container.add_structure('awesome', structure_mock)

        error_message = None
        try:
            container.add_structure('awesome', structure_mock)
        except core_exceptions.StructureNameConflictException, error:
            error_message = error.message

        self.assertEquals(
            'A structure with that name already exists.',
            error_message)


if __name__ == '__main__':
    unittest.main()
