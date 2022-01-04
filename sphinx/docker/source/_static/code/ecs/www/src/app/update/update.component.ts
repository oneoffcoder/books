import { Component, OnInit } from '@angular/core';
import {ApiService} from "../api/service";
import {ActivatedRoute, Router} from "@angular/router";
import {Person, PersonUpdate} from "../api/model";
import {filter, map, mergeMap} from "rxjs/operators";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UpdateComponent implements OnInit {

  formGroup: FormGroup;
  person?: Person;
  updated = false;

  constructor(private api: ApiService, private router: Router, private route: ActivatedRoute, private fb: FormBuilder) {
    this.formGroup = fb.group({
      firstName: ['', Validators.required],
      lastName: ['', Validators.required],
      gender: ['', Validators.required],
      age: ['', Validators.required]
    });
    this.person = undefined;
  }

  ngOnInit(): void {
    this.route.queryParams.pipe(
      filter(p => p['personId']),
      map(p => p['personId']),
      mergeMap(id => this.api.getPersonById(id))
    ).subscribe(
      p => {
        this.person = p;
        this.formGroup.patchValue({
          firstName: p.first_name,
          lastName: p.last_name,
          gender: p.gender,
          age: p.age
        });
      },
      e => {
        this.person = undefined;
        console.error(e);
      }
    );
  }

  onSubmit(): void {
    if (this.person && this.formGroup.status === 'VALID') {
      const p = new PersonUpdate(
        this.formGroup.value.firstName,
        this.formGroup.value.lastName,
        this.formGroup.value.gender,
        this.formGroup.value.age
      );

      this.api.updatePerson(this.person.id, p)
        .subscribe(
          r => {
            console.log(r);
            this.person = undefined;
            this.updated = true;
          },
          e => console.error(e)
        );
    }
  }

  cancelUpdate(): void {
    this.router.navigate(['/default']);
  }

}
