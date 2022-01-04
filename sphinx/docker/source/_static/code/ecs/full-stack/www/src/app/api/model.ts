export class PersonBase {
  constructor(public first_name: string, public last_name: string, public gender: string, public age: number) {

  }
}

export class PersonCreate extends PersonBase {
  constructor(first_name: string, last_name: string, gender: string, age: number) {
    super(first_name, last_name, gender, age);
  }
}

export class PersonUpdate extends PersonBase {
  constructor(first_name: string, last_name: string, gender: string, age: number) {
    super(first_name, last_name, gender, age);
  }
}

export class Person extends PersonBase {
  constructor(public id: number, first_name: string, last_name: string, gender: string, age: number) {
    super(first_name, last_name, gender, age);
  }
}

export class Message {
  constructor(public status: string, public content: string) {
  }
}
