class CoreException(Exception):
    pass


class StateVectorAlreadyGenerated(CoreException):
    pass


class StructureNameConflictException(CoreException):
    pass
