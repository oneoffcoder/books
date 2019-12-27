export class Student {
    id: number;
    firstName: string;
    lastName: string;
    gender: string

    constructor(id: number, firstName: string, lastName: string, gender: string) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.gender = gender;
    }

    public static toJson(student: Student): any {
        return {
            id: student.id,
            first_name: student.firstName,
            last_name: student.lastName,
            gender: student.gender
        }
    }

    public static fromJson(d: any): Student {
        return new Student(d.id, d.first_name, d.last_name, d.gender)
    }

    public static fromJsonArray(d: any): Array<Student> {
        return d.map(item => this.fromJson(item));
    }
}
