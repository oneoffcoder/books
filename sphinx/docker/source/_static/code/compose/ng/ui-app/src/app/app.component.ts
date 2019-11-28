import { Component, OnInit } from '@angular/core';
import { StudentService } from './service/student.service';
import { Student } from './bo/student';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  
  students: Array<Student>;
  createStudent: Student;
  updateStudent: Student;
  deleteId: number;
  errorCreating = false;
  errorUpdating = false;
  errorDeleting = false;

  constructor(private studentService: StudentService) { 
    this.createStudent = new Student(null, '', '', '');
    this.updateStudent = new Student(null, '', '', '');
  }

  ngOnInit(): void {
    this.readAll();
  }

  private readAll(): void {
    this.studentService.readAll()
      .subscribe(
        r => this.students = r, 
        e => console.error(e))
  }

  private create(): void {
    if (this.createStudent.firstName.length > 0 && 
      this.createStudent.lastName.length > 0 &&
      this.createStudent.gender.length > 0) {
        this.createStudent.gender = this.createStudent.gender.toLowerCase() === 'm' ? 'M' : 'F';
        this.studentService.create(this.createStudent)
          .subscribe(
            r => {
              this.createStudent = new Student(null, '', '', '');
              this.errorCreating = false;
              this.readAll();
            },
            e => {
              this.errorCreating = true;
            }
          )
      } else {
        this.errorCreating = true;
      }
  }

  private update(): void {
    if (this.updateStudent.firstName.length > 0 && 
      this.updateStudent.lastName.length > 0 &&
      this.updateStudent.gender.length > 0) {
        this.updateStudent.gender = this.updateStudent.gender.toLowerCase() === 'm' ? 'M' : 'F';
        this.studentService.update(this.updateStudent)
          .subscribe(
            r => {
              this.updateStudent = new Student(null, '', '', '');
              this.errorUpdating = false;
              this.readAll();
            },
            e => {
              this.errorUpdating = true;
            }
          )
      } else {
        this.errorUpdating = true;
      }
  }

  private delete(): void {
    if (this.deleteId) {
      try {
        const id = Number(this.deleteId);
        if (isNaN(id)) {
          throw new Error('');
        }
        console.log(`id is ${id}`);
        this.studentService.delete(id)
          .subscribe(
            r => {
              this.deleteId = undefined;
              this.errorDeleting = false;
              this.readAll();
            },
            e => {
              this.errorDeleting = true;
            }
          )
      } catch(e) {
        console.error(`${this.deleteId} is not a number`);
      }
    }    
  }

  private debug(): void {
    // this.studentService.readAll()
    //   .subscribe(r => {
    //     console.log(r)
    //     const x = r.map(s => Student.toJson(s));
    //     console.log(x);
    //   }, e => console.error(e))

    // this.studentService.read(1)
    //   .subscribe(r => console.log(r), e => console.error(e));

    // const student = Student.fromJson({ first_name: 'Zion', last_name: 'T', gender: 'M'});
    // console.log(`student=${student}`)
    // this.studentService.create(student)
    //   .subscribe(r => console.log(r), e => console.error(e));

    // const student = Student.fromJson({ id: 4, first_name: 'Zionx', last_name: 'T', gender: 'M'});
    // this.studentService.update(student)
    //   .subscribe(r => console.log(r), e => console.error(e));

    // this.studentService.delete(7)
    //   .subscribe(r => console.log(r), e => console.error(e));
  }
}
