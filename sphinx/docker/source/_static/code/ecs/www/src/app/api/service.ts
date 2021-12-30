import {environment} from './../../environments/environment';
import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private readonly healthUrl: string;
  private readonly personUrl: string;

  constructor(private http: HttpClient) {
    this.healthUrl = `${environment.apiService.urls.base}/${environment.apiService.urls.health}`;
    this.personUrl = `${environment.apiService.urls.base}/${environment.apiService.urls.person}`;
  }

  public getHealth(): Observable<any> {
      return this.http.get(this.healthUrl);
  }

  public getPerson(): Observable<any> {
      return this.http.get(this.personUrl);
  }
}
