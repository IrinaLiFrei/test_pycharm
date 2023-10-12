


class EmployeeName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        if not all([all(list(map(lambda x: x.isalpha(), name))) for name in value.split()]):
            raise ValueError(f'Name must contain only letters: {value}')
        if not all(map(lambda x: x.istitle(), value.split())):
            raise ValueError(f'Name must begin with the capital: {value}')
        setattr(instance, self.param_name, value)


class EmployeeID:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        if not len(value) == 6:
            raise ValueError(f'ID must be 6 digits: {value}')
        if not value.isdigit():
            raise ValueError(f'ID must contain only digits: {value}')
        setattr(instance, self.param_name, value)


# EXCEPTIONS


class OwnBasicException(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class LevelError(OwnBasicException):
    def __init__(self, me, new):
        super(LevelError, self).__init__(f'Access Level Error! Employee {me.name}, access level: {me.lvl_access} '
                                         f'is not authorized to hire or fire employee {new.name}, access level: {new.lvl_access} '
                                         f'with a higher access level')


class AccessError(OwnBasicException):
    def __init__(self, me):
        super(AccessError, self).__init__(f'Access Error! Employee {me.name} ({me.employee_id}) not found in database!')


class UniqueID(OwnBasicException):
    def __init__(self, new_id: str):
        super(UniqueID, self).__init__(f'Access Error! Employee with ID {new_id} already exists')

