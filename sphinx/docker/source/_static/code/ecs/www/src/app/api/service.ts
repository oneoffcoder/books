import {environment} from './../../environments/environment';
import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Message, Person, PersonCreate, PersonUpdate} from "./model";

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private readonly healthUrl: string;
  private readonly personUrl: string;

  constructor(private http: HttpClient) {
    // FIXME: remove later
    // const baseUrl = environment.apiService.urls.base.replace(':4200', '');
    const baseUrl = environment.apiService.urls.base;
    this.healthUrl = `${baseUrl}/${environment.apiService.urls.health}`;
    this.personUrl = `${baseUrl}/${environment.apiService.urls.person}`;
  }

  public getHealth(): Observable<any> {
      return this.http.get(this.healthUrl);
  }

  public createPerson(person: PersonCreate): Observable<Person> {
    return this.http.post<Person>(this.personUrl, person);
  }

  public getPersonById(id: number): Observable<Person> {
    const url = `${this.personUrl}/${id}`;
    return this.http.get<Person>(url);
  }

  public getPeople(skip = 0, limit = 10): Observable<Array<Person>> {
    const opts = {
      params: {skip, limit}
    };

    return this.http.get<Array<Person>>(this.personUrl, opts);
  }

  public updatePerson(id: number, person: PersonUpdate): Observable<Message> {
    const url = `${this.personUrl}/${id}`;
    return this.http.put<Message>(url, person);
  }

  public deletePerson(id: number): Observable<Message> {
    const url = `${this.personUrl}/${id}`;
    return this.http.delete<Message>(url);
  }
}
