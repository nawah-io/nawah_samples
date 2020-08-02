import { Component } from '@angular/core';
import { NawahService, Doc } from 'ng-nawah';
import { Router } from '@angular/router';

@Component({
  selector: 'page-admin-dashboard',
  templateUrl: 'admin-dashboard.page.html',
})
export class AdminDashboardPage {

  get user(): Doc {
    return this.nawah.session?.user;
  }

  constructor(private nawah: NawahService, private router: Router) { }

  signout(): void {
    this.nawah.signout().subscribe({
      next: (res) => {
        this.router.navigate(['/admin']);
      }
    })
  }

}