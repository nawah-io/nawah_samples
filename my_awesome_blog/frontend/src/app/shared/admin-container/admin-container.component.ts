import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { NawahService, Doc, Res } from 'ng-nawah';


@Component({
  selector: 'app-admin-container',
  template: `
    <router-outlet></router-outlet>
  `
})
export class AdminContainerComponent implements OnInit {

  constructor(private nawah: NawahService, private router: Router) { }

  ngOnInit() {
    try {
      this.nawah.checkAuth().subscribe({
        next: (res) => {
          console.log('re-authenticated!');
          if (this.router.url == '/admin/login') {
            this.router.navigate(['/admin', 'dashboard']);
          }
        },
        error: (res: Res<Doc>) => {
          if (this.router.url != '/admin/login') {
            this.router.navigate(['/admin']);
          }
        }
      });
    } catch (err) {
      if (this.router.url != '/admin/login') {
        this.router.navigate(['/admin']);
      }
    }
  }

}