import { Component, OnInit } from '@angular/core';
import {ApiService} from "../api/service";
import {ActivatedRoute, Router} from "@angular/router";
import { map, tap, mergeMap, mapTo, scan, filter, debounceTime, concatMap, expand, toArray} from 'rxjs/operators';
import {Person} from "../api/model";

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.scss']
})
export class DeleteComponent implements OnInit {

  person?: Person;
  deleted = false;

  constructor(private api: ApiService, private router: Router, private route: ActivatedRoute) {
    this.person = undefined;
  }

  ngOnInit(): void {
    this.route.queryParams.pipe(
      filter(p => p['personId']),
      map(p => p['personId']),
      mergeMap(id => this.api.getPersonById(id))
    ).subscribe(
      p => this.person = p,
      e => {
        this.person = undefined;
        console.error(e);
      }
    );
  }

  delete(): void {
    if (this.person) {
      const id = this.person.id;
      this.api.deletePerson(id)
        .subscribe(
          r => {
            this.deleted = true;
            console.log(`deleted: ${this.person?.id}`);
            this.person = undefined;
          },
          e => {
            console.log(e);
          }
        );
    }
  }

}
