from pydantic import BaseModel, EmailStr, conint, ValidationError, validator


class User(BaseModel):
    id: conint(gt=0)
    name: str
    email: EmailStr
    age: conint(ge=18, le=120)

    @validator('name')
    def name_must_have_space(cls, value):
        if ' ' not in value.strip():
            raise ValueError('full name must include a space')
        return value


def main():
    valid_data = {
        'id': 1,
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com',
        'age': 30,
    }

    invalid_data = {
        'id': 0,
        'name': 'Jane',
        'email': 'not-an-email',
        'age': 15,
    }

    try:
        user = User(**valid_data)
        print('Valid user:', user)
    except ValidationError as error:
        print('Validation failed for valid_data:')
        print(error)

    try:
        user = User(**invalid_data)
        print('Invalid user:', user)
    except ValidationError as error:
        print('Validation failed for invalid_data:')
        print(error)


if __name__ == '__main__':
    main()
