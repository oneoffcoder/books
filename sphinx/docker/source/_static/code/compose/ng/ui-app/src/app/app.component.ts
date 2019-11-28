import { Component, OnInit } from '@angular/core';
import { StudentService } from './service/student.service';
import { Student } from './bo/student';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  
  constructor(private studentService: StudentService) { 
    
  }

  ngOnInit(): void {
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
