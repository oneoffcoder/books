import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api/service';

@Component({
  selector: 'app-default',
  templateUrl: './default.component.html',
  styleUrls: ['./default.component.scss']
})
export class DefaultComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getHealth()
      .subscribe(
        r => console.log(r),
        e => console.error(e)
      );

    this.apiService.getPersonById(1)
      .subscribe(
        r => console.log(r),
        e => console.error(e)
      );
    this.apiService.getPeople()
      .subscribe(
        r => console.log(r),
        e => console.error(e)
      );
  }

}
