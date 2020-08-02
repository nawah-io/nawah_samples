import { Component } from '@angular/core';
import { Observable } from 'rxjs';

import { NawahService, Res } from 'ng-nawah';

@Component({
  selector: 'page-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.css'],
})
export class HomePage {

  blogs$: Observable<Res<any>> = this.nawah.call({
    endpoint: 'blog/read'
  });

  constructor(private nawah: NawahService) { }

}