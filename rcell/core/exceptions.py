class CoreException(Exception):
    pass


class StateVectorAlreadyGeneratedException(CoreException):
    pass


class StructureNameConflictException(CoreException):
    pass
