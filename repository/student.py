from ..model.student import Student
from ..lib.entityRepository.repository import RepositoryInterface
class StudentRepository(RepositoryInterface):
    def __init__(self) -> None:
        super().__init__(Student)
