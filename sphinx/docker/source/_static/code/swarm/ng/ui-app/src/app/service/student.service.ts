import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from './../../environments/environment';
import { Student } from './../bo/student';
import { Observable } from 'rxjs';
import {map} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class StudentService {

  private apiUrl = '';

  constructor(private http: HttpClient) { 
    console.log(`environment.apiUrl=${environment.apiUrl}`);
    this.apiUrl = environment.apiUrl;
  }

  private getHeaders(): HttpHeaders {
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    });
  }

  public readAll(): Observable<Array<Student>> {
    const url = `${this.apiUrl}/v1/students`;
    return this.http
      .get<Array<Student>>(url, {headers: this.getHeaders()})
      .pipe(
        map(r => Student.fromJsonArray(r))
      )
  }

  public create(student: Student): any {
    const url = `${this.apiUrl}/v1/student`;
    const body = Student.toJson(student)
    return this.http
      .post(url, body, {headers: this.getHeaders()})
  }

  public read(id: number): Observable<Student> {
    const url = `${this.apiUrl}/v1/student/${id}`;
    return this.http
        .get(url, {headers: this.getHeaders()})
        .pipe(
          map(r => Student.fromJson(r))
        )
  }

  public update(student: Student): any {
    const url = `${this.apiUrl}/v1/student/${student.id}`;
    const body = Student.toJson(student)
    return this.http
      .put(url, body, {headers: this.getHeaders()});
  }

  public delete(id: number): any {
    const url = `${this.apiUrl}/v1/student/${id}`;
    return this.http
      .delete(url, {headers: this.getHeaders()});
  }
}
